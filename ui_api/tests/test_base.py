from py_selenium_auto.browsers.browser_services import BrowserServices
from constants.constants import Constants
from integration_template.configurations.configuration import Configuration
import os


class TestBase:
    _AUTH_URL = 'http://{LOGIN}:{PASSWORD}@{START_URL}'
    _LOGIN = os.getenv(Constants.LOGIN)
    _PASSWORD = os.getenv(Constants.PASSWORD)

    def go_to_start_page(self):
        BrowserServices.Instance.browser.go_to(self._AUTH_URL.format(
            LOGIN=self._LOGIN, PASSWORD=self._PASSWORD, START_URL=Configuration.start_url()
        ))
        BrowserServices.Instance.browser.wait_for_page_to_load()
