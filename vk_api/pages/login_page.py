from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By
from py_selenium_auto.elements.button import Button
from py_selenium_auto.elements.text_box import TextBox


class LoginPage(Form):
    INDEX_LOGIN_ID = 'index_login'
    VK_ID_FORM_CLASS_NAME = 'VkIdForm'
    SIGNIN_BUTTON = '//*[contains(@class, "signInButton")]//*[contains(@class, "__in")]'
    INDEX_EMAIL_ID = 'index_email'

    def __init__(self):
        super().__init__(Locator(By.ID, self.INDEX_LOGIN_ID), 'Login page')
        self.label_nav_header = self._element_factory.get_label(
            Locator(By.CLASS_NAME, self.VK_ID_FORM_CLASS_NAME),
            'VK Id form'
        )

    def click_signin_button(self):
        self._form_element.find_child_element(
            Button,
            Locator.by_xpath(self.SIGNIN_BUTTON),
            "Sign in"
        ).wait_and_click()

    def send_email_to_text_field(self, email):
        self._form_element.find_child_element(TextBox
            ,
            Locator.by_id(self.INDEX_EMAIL_ID),
            "Send email to text field"
        ).type(email)
