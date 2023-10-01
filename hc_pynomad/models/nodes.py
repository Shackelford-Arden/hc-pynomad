from typing import Optional

from pydantic import Field
from pydantic import RootModel

from hc_pynomad.models.base import SimpleBase


class LastDrain(SimpleBase):
    accessor_id: str = Field(..., alias='AccessorID')
    meta: Optional[dict[str, str]] = Field(default_factory=dict, alias='Meta')
    started_at: str | None = Field(default=None, alias='StartedAt')
    status: str = Field(..., alias='Status')
    updated_at: str | None = Field(..., alias='UpdatedAt')


class HostNetwork(SimpleBase):
    name: str = Field(..., alias='Name')
    cidr: str = Field(..., alias='CIDR')
    reserved_ports: str = Field(..., alias='ReservedPorts')


class HostVolume(SimpleBase):
    name: str = Field(..., alias='Name')
    path: str = Field(..., alias='Path')
    read_only: bool = Field(..., alias='ReadOnly')


class Event(SimpleBase):
    create_index: int = Field(..., alias='CreateIndex')
    details: str | None = Field(default=None, alias='Details')
    message: str = Field(..., alias='Message')
    subsystem: str | None = Field(default=None, alias='Subsystem')
    timestamp: str = Field(..., alias='Timestamp')


class Driver(SimpleBase):
    attributes: Optional[dict[str, str]] = Field(default_factory=dict, alias='Attributes')
    detected: bool = Field(..., alias='Detected')
    health_description: str = Field(default_factory=str, alias='HealthDescription')
    healthy: bool = Field(..., alias='Healthy')
    update_time: str = Field(..., alias='UpdateTime')


class Node(SimpleBase):
    address: Optional[str] = Field(default_factory=str, alias='Address')
    attributes: Optional[dict[str, str]] = Field(default_factory=dict, alias='Attributes')
    computed_class: str | None = Field(default=None, alias='ComputedClass')
    create_index: int = Field(..., alias='CreateIndex')
    datacenter: str | list[str] = Field(..., alias='Datacenter')
    drain: bool = Field(..., alias='Drain')
    # drain_strategy:
    drivers: dict[str, Driver] = Field(default_factory=dict, alias='Drivers')
    events: list[Event] = Field(default_factory=list, alias='Events')
    http_addr: Optional[str] = Field(default_factory=str, alias='HTTPAddr')
    host_volumes: Optional[dict[str, HostVolume]] = Field(default_factory=dict, alias='HostVolumes')
    host_networks: Optional[dict[str, HostNetwork]] = Field(default_factory=dict, alias='HostNetworks')
    id: str = Field(..., alias='ID')
    last_drain: Optional[LastDrain] = Field(default=None, alias='LastDrain')
    links: Optional[dict[str, str]] = Field(default_factory=dict, alias='Links')
    meta: Optional[dict[str, str]] = Field(default_factory=dict, alias='Meta')
    modify_index: int = Field(..., alias='ModifyIndex')
    name: str = Field(..., alias='Name')
    node_class: Optional[str] = Field(default_factory=str, alias='NodeClass')
    node_pool: Optional[str] = Field(default_factory=str, alias='NodePool')
    node_resources: Optional[dict] = Field(default_factory=dict, alias='NodeResources')


class NodesList(RootModel):
    root: Optional[list[Node]] = Field(default_factory=list)
