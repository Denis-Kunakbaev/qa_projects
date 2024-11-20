from dataclasses import dataclass


@dataclass
class GetTokenParams:
    variant: int


@dataclass
class GetTestsResultParams:
    projectId: int


@dataclass
class AddTestToProjectParams:
    SID: str
    projectName: str
    testName: str
    methodName: str
    env: str
    startTime: str


@dataclass
class TestLog:
    testId: int
    content: str
