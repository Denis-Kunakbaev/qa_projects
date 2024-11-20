from models.results_model import TestResultModel
from constants.constants import Constants
from datetime import datetime


class ResultUpdater:

    @staticmethod
    def update_test_parameters(test_results):
        for test_result in test_results:
            updated_test_result = TestResultModel(
                name=test_result.name,
                method=test_result.method,
                status=test_result.status.upper(),
                startTime=datetime.strptime(test_result.startTime, Constants.START_TIME_PATTERN_FROM_WEB),
                endTime=test_result.endTime,
                duration=test_result.duration
            )

            test_results[test_results.index(test_result)] = updated_test_result

        return test_results
