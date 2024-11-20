from py_selenium_auto.elements.button import Button
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By


class VerificationForm(Form):
    VERIFICATION_MODAL = '//*[contains(@class, "vkuiModalPage__content-wrap")]'
    VERIFICATION_BY_PASSWORD_BUTTON = '//*[contains(@data-test-id, "verificationMethod_password")]'

    def __init__(self):
        super().__init__(
            Locator(By.XPATH, self.VERIFICATION_MODAL),
            "Verification form",
        )

    def click_password_method_button(self):
        self._form_element.find_child_element(
            Button,
            Locator.by_xpath(self.VERIFICATION_BY_PASSWORD_BUTTON),
            "Select password method"
        ).click()
