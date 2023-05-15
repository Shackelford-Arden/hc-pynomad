from pydantic import BaseModel
from pydantic import Field


class SimpleBase(BaseModel):
    class Config:
        allow_population_by_field_name = True


class Affinity(SimpleBase):
    attribute: str = Field(..., alias='Attribute')
    value: str = Field(..., alias='Value')
    weight: int = Field(..., alias='Weight')


class Constraint(SimpleBase):
    l_target: str = Field(..., alias='LTarget')
    operator: str = Field(..., alias='Operand')
    r_target: str = Field(..., alias='RTarget')


class RestartPolicy(SimpleBase):
    attempts: int = Field(..., alias='Attempts')
    interval: int = Field(..., alias='Interval')
    delay: int = Field(..., alias='Delay')
    mode: str = Field(..., alias='Mode')


class ReschedulePolicy(SimpleBase):
    attempts: int = Field(..., alias='Attempts')
    interval: int = Field(..., alias='Interval')
    delay: int = Field(..., alias='Delay')
    delay_function: str = Field(..., alias='constant')
    max_delay: int = Field(..., alias='MaxDelay')
    unlimited: bool = Field(default=False, alias='Unlimited')


class Spread(SimpleBase):
    attribute: str = Field(..., alias='Attribute')
    weight: int = Field(..., alias='Weight')
    spread_target: list[dict] = Field(default_factory=list, alias='SpreadTarget')
