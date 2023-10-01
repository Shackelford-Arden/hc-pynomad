from pydantic.dataclasses import dataclass

from hc_pynomad import Nomad
from hc_pynomad.models.nodes import NodesList


@dataclass
class Nodes(Nomad):
    """Client to interact with the /v1/nodes endpoint."""

    def list_nodes(self,
                   prefix: str = None, next_token: str = None,
                   per_page: int = 0, filter: str = None,
                   resources: bool = False, os: bool = False
                   ) -> NodesList:
        """
        API Docs: https://developer.hashicorp.com/nomad/api-docs/nodes#list-nodes

        Parameters
        ----------
        prefix: str = None
        next_token: str = None
        per_page: int = 0
        filter: str = None
        resources: bool = False
        os: bool = False

        Returns
        -------
        nodes: NodesList
        """

        params = {
            'resources': resources,
            'os': os
        }

        if prefix:
            params['prefix'] = prefix

        if next_token:
            params['next_token'] = next_token

        if per_page:
            params['per_page'] = per_page

        if filter:
            params['filter'] = filter

        results = self.call(endpoint='/nodes', verb='GET', params=params).json()

        return NodesList.model_validate(results)

    def read_node(self):
        """
        API Docs: https://developer.hashicorp.com/nomad/api-docs/nodes#read-node

        Parameters
        ----------

        Returns
        -------

        """
        pass

    def list_node_allocations(self):
        """
        API Docs: https://developer.hashicorp.com/nomad/api-docs/nodes#list-node-allocations

        Parameters
        ----------

        Returns
        -------

        """
        pass

    def create_node_evaluation(self):
        """
        API Docs: https://developer.hashicorp.com/nomad/api-docs/nodes#create-node-evaluation

        Parameters
        ----------

        Returns
        -------

        """
        pass

    def drain_node(self):
        """
        API Docs: https://developer.hashicorp.com/nomad/api-docs/nodes#drain-node

        Parameters
        ----------

        Returns
        -------

        """
        pass

    def purge_node(self):
        """
        API Docs: https://developer.hashicorp.com/nomad/api-docs/nodes#purge-node

        Parameters
        ----------

        Returns
        -------

        """
        pass

    def toggle_node_eligibility(self):
        """
        API Docs: https://developer.hashicorp.com/nomad/api-docs/nodes#toggle-node-eligibility

        Parameters
        ----------

        Returns
        -------

        """
        pass
