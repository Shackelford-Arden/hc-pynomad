from typing import List, Union

import httpx
from httpx import HTTPStatusError
from pydantic import Field
from pydantic.dataclasses import dataclass

from pynomad.exceptions.base import Unauthenticated, UnknownResourceCalled


@dataclass
class Nomad:
    address: str = Field(default="http://localhost:4646", env='NOMAD_ADDR', description='Base address for Nomad cluster/host.')
    token: str = Field(default=None, env='NOMAD_TOKEN', description='Valid Nomad token.')
    namespace: str = Field(default=None, env='NOMAD_NAMESPACE', description='Nomad namespace to use for querying resources.')
    headers: dict = Field(default={}, description='Custom headers to include on each request.')

    def _get(self, endpoint: str) -> Union[dict, str, List[str]]:
        """
        Specifically making GET requests to Nomad that expect JSON.

        Parameters
        ----------
        endpoint: str
            The specific endpoint to hit.

        Returns
        -------
        response: Union[dict, str, List[str]]

        Raises
        ------
        HTTPStatusError
        """

        if self.token:
            self.headers.update(
                {
                    'X-Nomad-Token': self.token
                }
            )

        params = {}
        if self.namespace:
            params = {'namespace': self.namespace}

        url = f'{self.address}/v1{endpoint}'
        try:

            response = httpx.get(url, headers=self.headers, params=params)

            response.raise_for_status()

        # Attempt to gracefully handle Nomad's documented response codes with helpful exceptions
        # https://www.nomadproject.io/api-docs#http-response-codes
        except HTTPStatusError as http_error:
            if http_error.response.status_code == 403:
                raise Unauthenticated('API called failed to due being unauthenticated. Maybe your token expired?')
            if http_error.response.status_code == 404:
                raise UnknownResourceCalled(
                    f'Called {http_error.request.url.raw_path} but received a 404. Check supported APi endpoints for your version of Nomad.'
                )
            raise http_error

        return response.json()


@dataclass
class NomadStatus(Nomad):
    def get_leader(self) -> str:
        """
        Calls the Nomad cluster and retrieves the current leader.

        Returns
        -------
        leader: str
            Returns the current leader's IP address and port.
        """

        return str(self._get(endpoint='/status/leader'))

    def list_peers(self) -> List[str]:
        """
        Obtains the cluster's peers.

        Returns
        -------
        peers: List[str]
        """
        peers: List[str] = []

        response = httpx.get(f'{self.address}/v1/status/peers').json()
        if isinstance(response, list):
            peers.extend(response)

        return peers
