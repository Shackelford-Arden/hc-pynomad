from pydantic import BaseModel
from pydantic import Field


class LastDrain(BaseModel):
    pass


class HostNetwork(BaseModel):
    name: str = Field(..., alias='Name')
    cidr: str = Field(..., alias='CIDR')
    reserved_ports: str = Field(..., alias='ReservedPorts')


class HostVolume(BaseModel):
    name: str = Field(..., alias='Name')
    path: str = Field(..., alias='Path')
    read_only: bool = Field(..., alias='ReadOnly')


class Event(BaseModel):
    create_index: int = Field(..., alias='CreateIndex')
    details: str | None = Field(default=None, alias='Details')
    message: str = Field(..., alias='Message')
    subsystem: str | None = Field(default=None, alias='Subsystem')
    timestamp: str = Field(..., alias='Timestamp')


class Driver(BaseModel):
    attributes: dict[str, str] = Field(default_factory=dict, alias='Attributes')
    detected: bool = Field(..., alias='Detected')
    health_description: str = Field(default_factory=str, alias='HealthDescription')
    healthy: bool = Field(..., alias='Healthy')
    update_time: str = Field(..., alias='UpdateTime')


class Node(BaseModel):
    attributes: dict[str, str] = Field(default_factory=dict, alias='Attributes')
    computed_class: str | None = Field(default=None, alias='ComputedClass')
    create_index: int = Field(..., alias='CreateIndex')
    datacenter: str | list[str] = Field(..., alias='Datacenter')
    drain: bool = Field(..., alias='Drain')
    # drain_strategy:
    drivers: dict[str, Driver] = Field(default_factory=dict, alias='Drivers')
    events: list[Event] = Field(default_factory=list, alias='Events')
    http_addr: str = Field(..., alias='HTTPAddr')
    host_volumes: dict[str, HostVolume] = Field(default_factory=dict, alias='HostVolumes')
    host_networks: dict[str, HostNetwork] = Field(default_factory=dict, alias='HostNetworks')
    id: str = Field(..., alias='ID')
    last_drain: str | None = Field(default=None, alias='LastDrain')

