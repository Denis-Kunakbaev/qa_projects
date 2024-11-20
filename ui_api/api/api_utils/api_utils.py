import dataclasses
import json

from constants.endpoints import Endpoints
from integration_template.configurations.configuration import Configuration
from api.api_utils.requests_manager import RequestManager
from models.config_model import ConfigModel
from models.requests_model import *
from constants.constants import Constants
from tests.test_utils.data_reader import DataReader
from models.results_model import TestResultModel
from tests.test_utils.xml_to_json_converter import XmlParser


class ApiUtils:
    config = ConfigModel.from_dict(DataReader(Constants.CONFIG).get_data())

    def __init__(self):
        self.__api_url = Configuration.api_url()
        self.__request_manager = RequestManager(self.__api_url)
        self.method_name = None

    def _make_request(self, method, test_id=None, json=None, **kwargs):
        params = {**kwargs}
        if test_id:
            method += Constants.TEST_ID_PARAM.format(test_id=test_id)
        response = self.__request_manager.send_request(method, params=params, json=json)
        return response

    def get_token(self):
        params = GetTokenParams(variant=self.config.variant)
        params_dict = dataclasses.asdict(params)
        response = self._make_request(Endpoints.GET_TOKEN, **params_dict)
        return response

    def get_tests_result(self):
        params = GetTestsResultParams(projectId=self.config.projectId)
        params_dict = dataclasses.asdict(params)
        response = self._make_request(Endpoints.GET_TESTS_JSON, **params_dict)
        try:
            tests_results = json.loads(response.text)
            return [TestResultModel.from_dict(test) for test in tests_results]
        except json.JSONDecodeError:
            return XmlParser.xml_to_json(response.text)

    def add_test_to_project(self, sid, project_name, test_name, start_time):
        self.method_name = self.add_test_to_project.__name__
        params = AddTestToProjectParams(SID=sid,
                                        projectName=project_name,
                                        testName=test_name,
                                        methodName=self.add_test_to_project.__name__,
                                        env=Constants.ENVIRONMENT,
                                        startTime=start_time)
        params_dict = dataclasses.asdict(params)
        response = self._make_request(Endpoints.CREATE_TEST_NOTE, **params_dict)
        return response.text

    def send_test_logs(self, test_id, logs):
        params = TestLog(testId=test_id, content=logs)
        params_dict = dataclasses.asdict(params)
        response = self._make_request(Endpoints.SEND_TEST_LOGS,
                                      **params_dict)
        return response

    def send_test_attachment(self, test_id, attachment):
        payload = {"content": attachment, "contentType": Constants.CONTENT_TYPE}
        response = self._make_request(Endpoints.SEND_TEST_ATTACHMENT,
                                      test_id=test_id,
                                      json=payload)
        return response
