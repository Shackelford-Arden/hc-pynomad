from pydantic.dataclasses import dataclass

from hc_pynomad.models.nodes import Node


@dataclass
class NodeDrain:
    node: Node

    def __enter__(self):
        pass

    def __exit__(self):
        pass
