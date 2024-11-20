import pytest
import os
from datetime import datetime

from crud_models.project_model import Project
from crud_models.status_model import Status
from crud_models.table_test_model import Test
from data_models.test_data_model import TestDataModel
from utils.json_reader import JsonHelper
from crud_models.db_manager import DatabaseManager
from constants.constants import Constants

root_dir = os.path.dirname(os.path.abspath(__file__))
test_data_path = os.path.join(root_dir, Constants.TEST_DATA_PATH)
test_data = TestDataModel(**JsonHelper(test_data_path).get_data())


@pytest.fixture(scope="module")
def db_manager():
    manager = DatabaseManager(test_data.host,
                              test_data.user,
                              test_data.password,
                              test_data.database)
    yield manager


@pytest.fixture(scope="module")
def project_model(db_manager):
    return Project(db_manager)


@pytest.fixture(scope="module")
def status_model(db_manager):
    return Status(db_manager)


@pytest.fixture(scope="module")
def table_test_model(db_manager):
    return Test(db_manager)


@pytest.fixture
def time_tracker():
    start_time = datetime.now()

    def get_elapsed_time():
        return datetime.now() - start_time

    yield start_time, get_elapsed_time
