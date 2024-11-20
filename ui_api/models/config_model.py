from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin


@dataclass
class ConfigModel(DataClassJsonMixin):
    startUrl: str
    apiUrl: str
    variant: int
    projectId: int
    headers: dict
