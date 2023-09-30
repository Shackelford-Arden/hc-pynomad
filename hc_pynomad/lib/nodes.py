from pydantic.dataclasses import dataclass

from hc_pynomad import Nomad


@dataclass
class Nodes(Nomad):
    """Client to interact with the /v1/nodes endpoint."""

    def list_nodes(self):
        """
        API Docs: https://developer.hashicorp.com/nomad/api-docs/nodes#list-nodes

        Parameters
        ----------

        Returns
        -------

        """
        pass

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
