from utils.id_generator import IdGenerator
from utils.string_generator import RandomTextGenerator
from utils.number_generator import NumberGenerator
from utils.even_number_checker import EvenNumberChecker
from data_models.tables_data_models import TestModel, ProjectModel
from constants.constants import Constants
import time


class TestDataBase:

    def test_run_test_case_1(self, table_test_model, project_model, status_model, time_tracker):
        start_time, get_elapsed_time = time_tracker
        actual_start_time = start_time.strftime(Constants.TIME_PATTERN)
        number = NumberGenerator.generate_random_number()
        status_name = Constants.STATUS_OK if EvenNumberChecker.is_even_number(number) else Constants.STATUS_FAILED
        status_id = status_model.get_by_name(status_name)[0]
        projects_count = len(project_model.get())
        project_id = IdGenerator.generate_random_id_for_project(projects_count)
        time.sleep(1)
        actual_end_time = (start_time + get_elapsed_time()).strftime(Constants.TIME_PATTERN)
        test = table_test_model.create(name=RandomTextGenerator.get_random_text(message_length=10),
                                       status_id=status_id,
                                       method_name=RandomTextGenerator.get_random_text(message_length=10),
                                       project_id=project_id,
                                       session_id=Constants.SESSION_ID,
                                       start_time=actual_start_time,
                                       end_time=actual_end_time,
                                       env=RandomTextGenerator.get_random_text(message_length=10),
                                       browser=Constants.BROWSER)
        assert test is not None, "Failed to create test"
        created_test_data = table_test_model.get(test)
        created_test = TestModel(*created_test_data[1:])
        assert created_test.status_id == status_id, \
            f"Test status is incorrect. Expected: {status_id}, Actual: {created_test.status_id}"

    def test_run_test_case_2(self, table_test_model, project_model, status_model, time_tracker):

        test_ids = IdGenerator.generate_random_id_with_repeating_digits()
        copied_test_ids = []

        for test_id in test_ids:
            start_time, get_elapsed_time = time_tracker
            actual_start_time = start_time.strftime(Constants.TIME_PATTERN)
            projects_count = len(project_model.get())
            project = ProjectModel(*project_model.get(IdGenerator.generate_random_id_for_project(projects_count)))
            number = NumberGenerator.generate_random_number()
            status_name = Constants.STATUS_OK if EvenNumberChecker.is_even_number(number) else Constants.STATUS_FAILED
            status_id = status_model.get_by_name(status_name)[0]
            time.sleep(1)
            actual_end_time = (start_time + get_elapsed_time()).strftime(Constants.TIME_PATTERN)
            test_data = table_test_model.get(test_id)
            test_id, copied_test = test_data[0], TestModel(*test_data[1:])
            project_id = project.id
            new_test_id = table_test_model.create(name=copied_test.name,
                                                  status_id=status_id,
                                                  method_name=copied_test.method_name,
                                                  project_id=project_id,
                                                  session_id=copied_test.session_id,
                                                  start_time=actual_start_time,
                                                  end_time=actual_end_time,
                                                  env=Constants.AUTHOR_NAME,
                                                  browser=Constants.BROWSER)
            updated_test = TestModel(*table_test_model.get()[-1][1:])
            assert copied_test != updated_test, "Test was not updated"
            copied_test_ids.append(new_test_id)

        test_table_size = len(table_test_model.get())
        for test_id in copied_test_ids:
            table_test_model.delete(test_id)
        assert len(table_test_model.get()) != test_table_size, "Not all copied tests were deleted."
