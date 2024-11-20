from dataclasses import dataclass


@dataclass
class TestDataModel:
    host: str
    user: str
    password: str
    database: str
