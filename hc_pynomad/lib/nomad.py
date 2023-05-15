import os
from functools import partial
from typing import Any, Optional

import httpx
from httpx import HTTPStatusError
from pydantic import Field
from pydantic.dataclasses import dataclass

from hc_pynomad.exceptions.base import Unauthenticated, UnknownResourceCalled


@dataclass
class Nomad:
    address: str = Field(
        default_factory=partial(os.getenv, 'NOMAD_ADDR', 'http://localhost:4646'),
        description='Base address for Nomad cluster/host.'
    )
    token: str = Field(
        default_factory=partial(os.getenv, 'NOMAD_TOKEN', ''),
        description='Valid Nomad token.'
    )
    namespace: str = Field(
        default_factory=partial(os.getenv, 'NOMAD_NAMESPACE', ''),
        description='Nomad namespace to use for querying resources.'
    )
    headers: Optional[dict] = Field(default_factory=dict, description='Custom headers to include on each request.')

    def call(self, endpoint: str, verb: str, **kwargs) -> Any:
        """
        Generic call to the Nomad API.

        Parameters
        ----------
        endpoint: str
        verb: str
        **kwargs
            Anything passed here is passed to the HTTPX Client kwargs.

        Returns
        -------
        Any
            This is generally the result of calling `.json()` on httpx.Response.
            Each endpoint/method should give more specific type hints.
        """

        if not endpoint.startswith('/'):
            endpoint = f'/{endpoint}'

        if self.token:
            self.headers['X-Nomad-Token'] = self.token

        params = {}
        if 'params' in kwargs.keys():
            params = kwargs.get('params')

        if not params.get('namespace') and self.namespace:
            params['namespace'] = self.namespace

        url = f'{self.address}/v1{endpoint}'

        try:

            with httpx.Client(headers=self.headers) as client:
                response = client.request(
                    method=verb.upper(),
                    url=url, headers=self.headers,
                    params=params,
                    **kwargs
                )

            response.raise_for_status()

        # Attempt to gracefully handle Nomad's documented response codes with helpful exceptions
        # https://www.nomadproject.io/api-docs#http-response-codes
        except HTTPStatusError as http_error:
            if http_error.response.status_code == 403:
                raise Unauthenticated('API called failed to due being unauthenticated. Maybe your token expired?')
            if http_error.response.status_code == 404:
                raise UnknownResourceCalled(
                    f'Called {http_error.request.url.raw_path} but received a 404.'
                    f' Check supported API endpoints for your version of Nomad.'
                )
            raise http_error

        return response.json()
