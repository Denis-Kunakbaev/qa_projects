from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By
from py_selenium_auto.elements.label import Label


class DetailsPage(Form):
    MAIN_CONTAINER = '//*[contains(@class, "container main-container")]'
    DETAILS_XPATH = '//*[contains(@class, "list-group-item-text") and contains(text(), "{detail}")]'
    IMAGE_LINK = '//*[contains(@class, "table")]//a'
    START_TIME = '//*[contains(text(), "Start time")]'
    ENVIRONMENT = '//*[contains(text(), "{env}")]'
    LOGS = '//*[contains(text(), "Logs")]/following-sibling::*//td'

    def __init__(self):
        super().__init__(Locator(By.XPATH, self.MAIN_CONTAINER), 'Added project page')

    def get_test_name(self, test_name):
        return self._form_element.find_child_element(
            Label,
            Locator(By.XPATH, self.DETAILS_XPATH.format(detail=test_name)),
            "Check test name"
        ).text

    def get_project_name(self, project_name):
        return self._form_element.find_child_element(
            Label,
            Locator(By.XPATH, self.DETAILS_XPATH.format(detail=project_name)),
            "Get project name"
        ).text

    def get_method_name(self, method_name):
        return self._form_element.find_child_element(
            Label,
            Locator(By.XPATH, self.DETAILS_XPATH.format(detail=method_name)),
            "Get method name"
        ).text

    def get_start_time(self):
        return self._form_element.find_child_element(
            Label,
            Locator(By.XPATH, self.START_TIME),
            "Get start time"
        ).text.lstrip('Start time: ')

    def get_img_link(self):
        return self._form_element.find_child_element(
            Label,
            Locator(By.XPATH, self.IMAGE_LINK),
            "Download image"
        ).get_attribute('href')

    def get_environment(self, env):
        return self._form_element.find_child_element(
            Label,
            Locator(By.XPATH, self.ENVIRONMENT.format(env=env)),
            "Get environment"
        ).text

    def get_logs(self):
        return self._form_element.find_child_element(
            Label,
            Locator(By.XPATH, self.LOGS),
            "Get logs"
        ).text
