from py_selenium_auto.browsers.browser_services import BrowserServices

from integration_template.configurations.configuration import Configuration


class TestBase:

    def go_to_start_page(self):
        BrowserServices.Instance.browser.go_to(Configuration.start_url())
        BrowserServices.Instance.browser.wait_for_page_to_load()
