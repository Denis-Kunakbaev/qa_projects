from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By
from py_selenium_auto.elements.text_box import TextBox
from py_selenium_auto.elements.button import Button


class AddProjectForm(Form):
    ADD_PROJECT_FORM_ID = 'addProjectForm'
    TEXT_FIELD = 'projectName'
    SAVE_PROJECT_BUTTON = 'btn btn-primary'
    INFO_MESSAGE = '//*[contains(@class, "alert")]'

    def __init__(self):
        super().__init__(
            Locator(By.ID, self.ADD_PROJECT_FORM_ID),
            "Verification form",
        )

    def send_project_name(self, text):
        self._form_element.find_child_element(
            TextBox,
            Locator.by_id(self.TEXT_FIELD),
            "Send project name"
        ).send_keys(text)

    def save_project(self):
        self._form_element.find_child_element(
            Button,
            Locator.by_class_name(self.SAVE_PROJECT_BUTTON),
            "Save project"
        ).click_and_wait()

    def get_info_message(self):
        return self._form_element.find_child_element(
            TextBox,
            Locator.by_xpath(self.INFO_MESSAGE),
            "Get info message"
        ).text
