from dataclasses import dataclass
from datetime import datetime


@dataclass
class DetailsModel:
    project_name: str
    test_name: str
    method_name: str
    environment: str
    start_time: datetime
    logs: str
    image: str