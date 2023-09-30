
from typing import Optional

from pydantic import BaseModel
from pydantic import Field
from pydantic import field_validator


class Member(BaseModel):
    name: str = Field(..., alias='Name')
    addr: str = Field(..., alias='Addr')
    port: int = Field(..., alias='Port')
    tags: dict = Field(default_factory=dict, alias='Tags')
    status: str = Field(..., alias='Status')
    protocol_min: int = Field(..., alias='ProtocolMin')
    protocol_max: int = Field(..., alias='ProtocolMax')
    protocol_cur: int = Field(..., alias='ProtocolCur')
    delegate_min: int = Field(..., alias='DelegateMin')
    delegate_max: int = Field(..., alias='DelegateMax')
    delegate_cur: int = Field(..., alias='DelegateCur')

    @field_validator('tags', mode='before')
    def null_dict(cls, value):
        if value is None:
            return {}
        return value

    @field_validator('addr', mode='before')
    def empty_addr(cls, value):
        if value is None:
            return ""
        return value


class Members(BaseModel):
    server_name: str = Field(..., alias='ServerName')
    server_region: str = Field(..., alias='ServerRegion')
    server_dc: str = Field(..., alias='ServerDC')
    members: list[Member] = Field(default_factory=list, alias='Members')


class Addresses(BaseModel):
    http: str = Field(..., alias='HTTP')
    rpc: str = Field(..., alias='RPC')
    serf: str = Field(..., alias='Serf')


class Reserved(BaseModel):
    cpu: int = Field(..., alias='CPU')
    cores: int = Field(..., alias='Cores')
    disk_mb: int = Field(..., alias='DiskMB')
    memory_mb: int = Field(..., alias='MemoryMB')
    parsed_reserved_ports: Optional[list] = Field(default_factory=list, alias='ParsedReservedPorts')

    @field_validator('parsed_reserved_ports', mode='before')
    def null_reserved_ports(cls, value):
        if value is None:
            return []
        return value


class ConfigClient(BaseModel):
    alloc_dir: str = Field(..., alias='AllocDir')
    chroot_env: Optional[dict] = Field(default_factory=dict, alias='ChrooEnv')
    client_max_port: int = Field(..., alias='ClientMaxPort')
    client_min_port: int = Field(..., alias='ClientMinPort')
    disable_remote_exec: bool = Field(default=False, alias='DisableRemoteExec')
    enabled: bool = Field(..., alias='Enabled')
    gc_disk_usage_threshold: int = Field(..., alias='GCDiskUsageThreshold')
    gc_inode_usage_threshold: int = Field(..., alias='GCInodeUsageThreshold')
    gc_interval: int = Field(..., alias='GCInterval')
    max_kill_timeout: str = Field(..., alias='MaxKillTimeout')
    meta: dict = Field(..., alias='Meta')
    network_interface: str = Field(..., alias='NetworkInterface')
    network_speed: int = Field(..., alias='NetworkSpeed')
    node_class: str = Field(..., alias='NodeClass')
    options: dict = Field(..., alias='Options')


class AgentACL(BaseModel):
    enabled: bool = Field(..., alias='Enabled')
    policy_ttl: int = Field(..., alias='PolicyTTL')
    replication_token: str = Field(..., alias='ReplicationToken')
    token_ttl: int = Field(..., alias='TokenTTL')


class AgentAuditConfig(BaseModel):
    enabled: bool = Field(default=False, alias='Enabled')
    filters: list = Field(default_factory=list, alias='Filters')
    sinks: list = Field(default_factory=list, alias='Sinks')

    @field_validator('enabled', mode='before')
    def enabled_null(cls, value):
        if value is None:
            return False
        return value

    @field_validator('filters', 'sinks', mode='before')
    def null_lists(cls, value):
        if value is None:
            return []
        return value


class AgentConfig(BaseModel):
    acl: Optional[AgentACL] = Field(None, efault=None, alias='ACL')
    addresses: Addresses = Field(..., alias='Addresses')
    advertised_addrs: Addresses = Field(..., alias='AdvertiseAddrs')
    audit: AgentAuditConfig = Field(..., alias='Audit')
    autopilot: dict = Field(..., alias='Autopilot')
    bind_addr: str = Field(..., alias='BindAddr')
    client: dict = Field(..., alias='Client')


class StatsClient(BaseModel):
    node_id: str = Field(..., alias='node_id')
    known_servers: str = Field(..., alias='known_servers')
    num_allocations: str = Field(..., alias='num_allocations')
    last_heartbeat: str = Field(..., alias='last_heartbeat')
    heartbeat_ttl: str = Field(..., alias='heartbeat_ttl')


class StatsRuntime(BaseModel):
    max_procs: str = Field(..., alias='max_procs')
    goroutines: str = Field(..., alias='goroutines')
    cpu_count: str = Field(..., alias='cpu_count')
    kernel_name: str = Field(..., alias='kernel.name')
    arch: str = Field(..., alias='arch')
    version: str = Field(..., alias='version')


class SelfStats(BaseModel):
    client: StatsClient
    runtime: StatsRuntime


class Self(BaseModel):
    config: AgentConfig = Field(..., alias='config')
    member: Member
    stats: SelfStats
