from dataclasses import dataclass
from typing import List

from httpx import HTTPStatusError

from pynomad.exceptions.base import NomadAgentError
from pynomad.lib.nomad import Nomad
from pynomad.models.agent_models import Members, Self


@dataclass
class NomadAgent(Nomad):
    """
    Used when specifically speaking to Nomad nodes themselves.

    Does not work when calling the Nomad servers.
    """

    _endpoint = '/agent'

    def list_members(self) -> Members:
        """
        Lists members of the cluster.

        Returns
        -------
        members: Members
        """

        raw_response = self._get(endpoint=f'{self._endpoint}/members')

        return Members.parse_obj(raw_response)

    def list_servers(self) -> List[str]:
        """
        Lists the cluster servers.

        Returns
        -------
        servers: List[str]
            List of servers in the cluster. Example: ["127.0.0.1:4647"]

        """

        try:
            raw_response = self._get(endpoint=f'{self._endpoint}/servers')
        except HTTPStatusError as http_error:
            if http_error.response.status_code == 501:
                raise NomadAgentError('Seems a Nomad server was called when only Clients support this call.')
            raise http_error

        servers = []
        if isinstance(raw_response, list):
            servers.extend(raw_response)

        return servers

    def self(self) -> Self:
        """
        Gets attributes for the given node.

        Returns
        -------
        self: Self
        """

        results = self._get(endpoint=f'{self._endpoint}/self')

        return Self.parse_obj(results)
