import httpx
from pydantic.dataclasses import dataclass

from hc_pynomad import Nomad


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

        return str(self.call(endpoint='/status/leader', verb='GET'))

    def list_peers(self) -> list[str]:
        """
        Obtains the cluster's peers.

        Returns
        -------
        peers: list[str]
        """
        peers: list[str] = []

        response = httpx.get(f'{self.address}/v1/status/peers').json()
        if isinstance(response, list):
            peers.extend(response)

        return peers
