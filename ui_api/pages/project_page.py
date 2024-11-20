from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By
from constants.constants import Constants
from py_selenium_auto.elements.button import Button
from py_selenium_auto.elements.label import Label
from models.results_model import TestResultModel


class ProjectPage(Form):
    MAIN_CONTAINER = '//*[contains(@class, "container main-container")]'
    PROJECT_HEADER = '//*[contains(text(), "{project_name}")]'
    TESTS_TABLE = 'table'
    TEST_DETAILS = '//*[contains(@href, "testInfo?testId={testid}")]'
    HOME_BUTTON = '//a[contains(text(), "Home")]'

    def __init__(self, project_name):
        super().__init__(Locator(By.XPATH, self.MAIN_CONTAINER), f'{project_name} project page')
        self.label_nav_header = self._element_factory.get_label(
            Locator(By.XPATH, self.PROJECT_HEADER.format(project_name=project_name)),
            f'{project_name} project'
        )
        self._lines = []
        self.get_columns_data()

    def get_table(self):
        return self._form_element.find_child_element(
            Label,
            Locator.by_class_name(self.TESTS_TABLE),
            'Table of tests'
        )

    def get_rows(self):
        return self.get_table().find_child_elements(
            Label,
            Locator.by_tag_name('tr'),
            'Rows of table')

    def get_columns_data(self):
        for row in self.get_rows()[1:]:
            cells = []
            cell = row.find_child_elements(
                Label,
                Locator.by_tag_name('td'),
            )
            for i in range(len(cell) - 1):
                cells.append(cell[i].text)
            self._lines.append(cells)

    def get_tests_result(self):
        return [TestResultModel(*i) for i in self._lines]

    def go_to_main_page(self):
        self._form_element.find_child_element(
            Button,
            Locator.by_css_selector(self.HOME_BUTTON),
            "Go to main page"
        ).click_and_wait()

    def take_screenshot(self):
        self._form_element._browser.driver.save_screenshot(Constants.TAKEN_IMAGE)

    def show_test_details(self, test_id):
        self._form_element.find_child_element(
            Button,
            Locator(By.XPATH, self.TEST_DETAILS.format(testid=test_id)),
            "Show test details"
        ).click_and_wait()
