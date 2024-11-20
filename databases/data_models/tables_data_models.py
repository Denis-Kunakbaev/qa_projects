from dataclasses import dataclass


@dataclass
class TestModel:
    name: str
    status_id: int
    method_name: str
    project_id: int
    session_id: int
    start_time: str
    end_time: str
    env: str
    browser: str
    author_id: bool

@dataclass
class StatusModel:
    id: int
    name: str

@dataclass
class ProjectModel:
    id: int
    name: str
