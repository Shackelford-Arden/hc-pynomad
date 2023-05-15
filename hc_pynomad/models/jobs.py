from typing import Optional

from pydantic import Field

from hc_pynomad.models.base import Affinity
from hc_pynomad.models.base import Constraint
from hc_pynomad.models.base import ReschedulePolicy
from hc_pynomad.models.base import RestartPolicy
from hc_pynomad.models.base import SimpleBase
from hc_pynomad.models.base import Spread


class Template(SimpleBase):
    source_path: str = Field(default_factory=str, alias='SourcePath')
    dest_path: str = Field(default_factory=str, alias='DestPath')
    template_content: str = Field(default_factory=str, alias='EmbeddedTmpl')


class ServiceCheck(SimpleBase):
    name: str = Field(..., alias='Name')
    command: str = Field(default_factory=str, alias='Command')
    args: list[str] = Field(default_factory=list, alias='Args')
    path: str = Field(default_factory=str, alias='Path')
    protocol: str = Field(default_factory=str, alias='Protocol')
    port_label: str = Field(default_factory=str, alias='PortLabel')


class DeviceResource(SimpleBase):
    name: str = Field(..., alias='Name')
    count: int = Field(..., alias='Count')
    constraints: Optional[list[Constraint]] = Field(default_factory=list, alias='Constraints')
    affinities: Optional[list[Affinity]] = Field(default_factory=list, alias='Affinities')


class TaskResources(SimpleBase):
    cpu: int = Field(..., alias='CPU')
    cores: Optional[int] = Field(default_factory=int, alias='Cores')
    memory_mb: int = Field(..., alias='MemoryMB')
    memory_max_mb: Optional[int] = Field(default_factory=int, alias='MemoryMaxMB')
    disk_mb: Optional[int] = Field(default_factory=int, alias='DiskMB')
    devices: Optional[list[DeviceResource]] = Field(default_factory=list, alias='Devices')


class ServiceConnect(SimpleBase):
    native: bool = Field(default=False, alias='Native')
    sidecar_service: dict = Field(default_factory=dict, alias='SidecarService')
    sidecar_task: dict = Field(default_factory=dict, alias='SidecarTask')
    gateway: dict = Field(default_factory=dict, alias='Gateway')


class Service(SimpleBase):
    name: str = Field(..., alias='Name')
    task_name: str = Field(default_factory=str, alias='TaskName')
    port_label: str = Field(default_factory=str, alias='PortLabel')
    address_mode: str = Field(..., alias='AddressMode')
    address: str = Field(..., alias='Address')
    enable_tag_override: bool = Field(default=False, alias='EnableTagOverride')
    tags: list[str] = Field(default_factory=list, alias='Tags')
    canary_tags: list[str] = Field(default_factory=list, alias='CanaryTags')
    checks: list[ServiceCheck] = Field(default_factory=list, alias='Checks')
    connect: Optional[ServiceConnect] = Field(default=None, alias='Connect')


class Lifecycle(SimpleBase):
    hook: str = Field(..., alias='Hook')
    sidecar: bool = Field(default=False, alias='Sidecar')


class TaskLogConfig(SimpleBase):
    max_files: int = Field(..., alias='MaxFiles')
    max_files_size_mb: int = Field(..., alias='MaxFileSizeMB')
    enabled: bool = Field(..., alias='Enabled')


class Artifact(SimpleBase):
    destination: str = Field(..., alias='Destination')
    mode: str = Field(..., alias='Mode')
    options: dict = Field(default_factory=dict, alias='Options')
    headers: dict = Field(default_factory=dict, alias='Headers')
    source: str = Field(..., alias='Source')


class VaultConfig(SimpleBase):
    policies: list[str] = Field(default_factory=list, alias='Policies')


class Identity(SimpleBase):
    env: bool = Field(default=True, alias='Env')
    file: bool = Field(default=True, alias='File')


class Task(SimpleBase):
    name: str = Field(..., alias='Name')
    driver: str = Field(..., alias='Driver')
    user: str = Field(default_factory=str, alias='User')
    lifecycle: Optional[Lifecycle] = Field(default=None, alias='Lifecycle')
    config: dict = Field(default_factory=dict, alias='Config')
    constraints: Optional[list[Constraint]] = Field(default_factory=list, alias='Constraints')
    affinities: Optional[list[Affinity]] = Field(default_factory=list, alias='Affinities')
    env: Optional[dict] = Field(default_factory=dict, alias='Env')
    services: Optional[list[Service]] = Field(default_factory=list, alias='Services')
    resources: Optional[TaskResources] = Field(default=None, alias='Resources')
    restart_policy: Optional[RestartPolicy] = Field(default=None, alias='RestartPolicy')
    meta: Optional[dict] = Field(default_factory=dict, alias='Meta')
    kill_timeout: Optional[int] = Field(default=None, alias='KillTimeout')
    log_config: Optional[TaskLogConfig] = Field(default=None, alias='LogConfig')
    artifacts: Optional[list[Artifact]] = Field(default_factory=list, alias='Artifacts')
    vault: Optional[VaultConfig] = Field(default_factory=VaultConfig, alias='Vault')
    templates: Optional[list[Template]] = Field(default_factory=list, alias='Templates')
    dispatch_payload: Optional[dict] = Field(default_factory=dict, alias='DispatchPayload')
    volume_mounts: Optional[list[dict]] = Field(default_factory=list, alias='VolumeMounts')
    leader: bool = Field(default=False, alias='Leader')
    shutdown_delay: int = Field(..., alias='ShutdownDelay')
    kill_signal: str = Field(default_factory=str, alias='KillSignal')
    kind: str = Field(default_factory=str, alias='Kind')
    scaling_policies: Optional[list[dict]] = Field(default_factory=list, alias='ScalingPolicies')
    identity: Identity = Field(..., alias='Identity')


class EphemeralDisk(SimpleBase):
    migrate: Optional[bool] = Field(default=False, alias='Migrate')
    size: int = Field(..., alias='SizeMB')
    sticky: Optional[bool] = Field(default=False, alias='Sticky')


class TaskGroup(SimpleBase):
    name: str = Field(..., alias='Name')
    count: int = Field(..., alias='Count')
    constraints: Optional[list[Constraint]] = Field(default_factory=list, alias='Constraints')
    affinities: Optional[list[Affinity]] = Field(default_factory=list, alias='Affinities')
    tasks: list[Task] = Field(..., alias='Tasks')
    spreads: list[Spread] = Field(default_factory=list, alias='')
    volumes: Optional[list[dict]] = Field(default_factory=list, alias='Volumes')
    restart_policy: Optional[RestartPolicy] = Field(default=None, alias='RestartPolicy')
    reschedule_policy: Optional[ReschedulePolicy] = Field(default=None, alias='ReschedulePolicy')
    ephemeral_disk: Optional[EphemeralDisk] = Field(default=None, alias='EphemeralDisk')


class Job(SimpleBase):
    region: Optional[str] = Field(default_factory=str, alias='Region')
    namespace: Optional[str] = Field(default_factory=str, alias='Namespace')
    id: str = Field(..., alias='ID')
    name: str = Field(..., alias='Name')
    type: str = Field(..., alias='Type')
    priority: Optional[int] = Field(default_factory=int, alias='Priority')
    all_at_once: Optional[bool] = Field(default=False, alias='AllAtOnce')
    datacenters: list[str] = Field(..., alias='Datacenters')
    constraints: Optional[list[Constraint]] = Field(default_factory=list, alias='Constraints')
    affinities: Optional[list[Affinity]] = Field(default_factory=list, alias='Affinities')
    task_groups: list[TaskGroup] = Field(default_factory=list, alias='TaskGroups')
