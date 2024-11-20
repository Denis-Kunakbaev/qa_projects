from py_selenium_auto.elements.button import Button
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By
from pages.forms.verification_form import VerificationForm
from py_selenium_auto.elements.text_box import TextBox


class AutorizationPage(Form):
    AUTORIZATION_ROOT = '//*[contains(@class, "vkuiSplitCol")]'
    AUTORIZATION_METHOD_BUTTON = '//*[contains(@class, "vkuiButton__in")]'
    PASSWORD_FIELD = '//*[contains(@type, "password")]'
    SUBMIT_BUTTON = '//*[contains(@type, "submit")]'

    def __init__(self):
        super().__init__(
            Locator(By.XPATH, self.AUTORIZATION_ROOT),
            "Autorization page",
        )
        self.verification_form = VerificationForm()

    def click_change_autorization_method_button(self):
        self._form_element.find_child_element(
            Button,
            Locator.by_xpath(self.AUTORIZATION_METHOD_BUTTON),
            "Change autorization method"
        ).click()

    def send_password_to_text_field(self, password):
        self._form_element.find_child_element(TextBox
            ,
            Locator.by_xpath(self.PASSWORD_FIELD),
            "Send password to text field"
        ).type(password)

    def click_submit_button(self):
        self._form_element.find_child_element(
            Button,
            Locator.by_xpath(self.SUBMIT_BUTTON),
            "Log in"
        ).wait_and_click()
