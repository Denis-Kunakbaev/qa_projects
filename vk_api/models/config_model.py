from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin


@dataclass
class ConfigModel(DataClassJsonMixin):
    startUrl: str
    apiUrl: str
    token: str
    version: str
    headers: dict
    email: str
    password: str
    user_name: str
