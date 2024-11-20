import allure
from datetime import datetime

from py_selenium_auto.browsers.browser_services import BrowserServices
from tests.test_base import TestBase
from api.api_utils.api_utils import ApiUtils
from pages.main_page import MainPage
from pages.project_page import ProjectPage
from models.cookies_model import CookiesModel
from pages.details_page import DetailsPage
from models.config_model import ConfigModel
from models.details_model import DetailsModel
from constants.constants import Constants

from tests.test_utils.data_reader import DataReader
from tests.test_utils.results_updater import ResultUpdater
from tests.test_utils.random_text_generator import RandomTextGenerator
from tests.test_utils.image_coder import ImageCoder
from tests.test_utils.file_loader import FileLoader
from tests.test_utils.strings_formatter import StringFormatter


class TestApiUi(TestBase):
    main_page = MainPage()
    api_utils = ApiUtils()
    config = ConfigModel.from_dict(DataReader(Constants.CONFIG).get_data())
    token = None
    SID = RandomTextGenerator.get_random_text(Constants.LENGHT_OF_RANDOM_TEXT)
    details_page = DetailsPage()
    file_loader = FileLoader()

    def setup(self):
        with allure.step('Go to main page'):
            self.token = self.api_utils.get_token().text
            assert self.token is not None, 'The token was not received'
            self.go_to_start_page()

        with allure.step('Main page is displayed'):
            assert self.main_page.state.wait_for_displayed(), 'The main page was not opened'
            assert self.main_page.label_nav_header.state.wait_for_displayed(), 'The header of main page was not opened'

    def test_api_ui(self):
        with allure.step('Get variant from footer'):
            cookies_model = CookiesModel(name=Constants.COOKIES_NAME, value=self.token)
            BrowserServices.Instance.browser.driver.add_cookie(cookies_model.__dict__)
            BrowserServices.Instance.browser.refresh()
            footer = self.main_page.get_footer().text
            assert str(self.config.variant) == footer[-1], 'The variant was not received'

        with allure.step('Go to Nexage project'):
            self.main_page.go_to_project(Constants.NEXAGE_PROJ)

        with allure.step('Nexage project page is displayed'):
            self.nexage_page = ProjectPage(Constants.NEXAGE_PROJ)
            self.nexage_page.state.wait_for_displayed()
            assert self.nexage_page.label_nav_header.state.wait_for_displayed(), \
                f'The {Constants.NEXAGE_PROJ} project page was not opened'

        with allure.step('Get tests results'):
            api_tests_results = ResultUpdater.update_test_parameters(self.api_utils.get_tests_result())
            web_tests_results = ResultUpdater.update_test_parameters(self.nexage_page.get_tests_result())
            assert web_tests_results == sorted(web_tests_results, key=lambda test: test.startTime, reverse=True), \
                'The tests results are not sorted'
            assert all(test in api_tests_results for test in web_tests_results), 'The tests results are not equal'

        with allure.step('Go to main page'):
            self.nexage_page.go_to_main_page()
            assert self.main_page.state.is_displayed(), 'The main page was not opened'

        with allure.step('Add new project'):
            self.main_page.add_new_project()
            proj_name = RandomTextGenerator.get_random_text(Constants.LENGHT_OF_RANDOM_TEXT)
            self.main_page.switch_to_new_tab_and_send_text(proj_name)
            self.main_page.add_project_form.save_project()
            assert proj_name in self.main_page.add_project_form.get_info_message(), \
                f'The project {proj_name} was not added'
            self.main_page.return_to_start_tab()
            BrowserServices.Instance.browser.refresh()
            assert proj_name in self.main_page.get_projects_list(), f'The project {proj_name} not in list'

        with allure.step('Go to added project page'):
            self.main_page.go_to_added_project_page(proj_name)
            self.added_project_page = ProjectPage(proj_name)

        with allure.step('Update test results'):
            logs = DataReader.get_logs()
            logs = StringFormatter.format_string_from_api(logs)
            start_time = datetime.now().strftime(Constants.START_TIME_PATTERN_FOR_LOAD)
            test_id = self.api_utils.add_test_to_project(self.SID, proj_name, self.__class__.__name__, start_time)
            self.added_project_page.label_nav_header.state.wait_for_displayed()
            self.api_utils.send_test_logs(test_id, logs)
            self.added_project_page.take_screenshot()
            image = ImageCoder.encode_image(Constants.TAKEN_IMAGE)
            self.api_utils.send_test_attachment(test_id, image)
            assert self.__class__.__name__ in self.added_project_page.get_table().text, 'The test was not added'

        with allure.step('Check test details'):
            self.added_project_page.show_test_details(test_id)
            test_name = self.__class__.__name__
            methdod_name = self.api_utils.method_name
            sended_data_model = DetailsModel(project_name=proj_name,
                                             test_name=self.__class__.__name__,
                                             method_name=methdod_name,
                                             environment=Constants.ENVIRONMENT,
                                             start_time=datetime.strptime(start_time,
                                                                          Constants.START_TIME_PATTERN_FOR_LOAD),
                                             logs=logs,
                                             image=image)
            web_logs = self.details_page.get_logs()
            web_logs = StringFormatter.format_string_from_web(web_logs)
            test_start_time = datetime.strptime(self.details_page.get_start_time(),
                                                Constants.START_TIME_PATTERN_FROM_WEB)
            assert test_start_time == datetime.strptime(start_time, Constants.START_TIME_PATTERN_FOR_LOAD), \
                'The start time is not correct'
            img_link = self.details_page.get_img_link()
            self.file_loader.download_image(img_link)
            downloaded_image = ImageCoder.encode_image(Constants.DOWNLOADED_IMAGE)
            web_data_model = DetailsModel(project_name=self.details_page.get_project_name(proj_name),
                                          test_name=self.details_page.get_test_name(test_name),
                                          method_name=self.details_page.get_method_name(methdod_name),
                                          environment=self.details_page.get_environment(Constants.ENVIRONMENT),
                                          start_time=test_start_time,
                                          logs=web_logs,
                                          image=downloaded_image)
            assert sended_data_model == web_data_model, 'Values are not equal'
