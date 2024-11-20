from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin


@dataclass
class TestResultModel(DataClassJsonMixin):
    name: str = None
    method: str = None
    status: str = None
    startTime: str = None
    endTime: str = ''
    duration: str = None
