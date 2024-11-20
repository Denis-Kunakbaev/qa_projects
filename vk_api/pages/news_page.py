from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By
from py_selenium_auto.elements.button import Button


class NewsPage(Form):
    SIDE_BAR = '//*[contains(@class, "side_bar_inner")]'
    NEWS_FILTER_ID = 'ui_rmenu_news'
    PROFILE_BUTTON = '//*[@id="l_pr"]/a'

    def __init__(self):
        super().__init__(Locator(By.XPATH, self.SIDE_BAR), 'Side bar')
        self.label_nav_header = self._element_factory.get_label(
            Locator(By.ID, self.NEWS_FILTER_ID),
            'News page'
        )

    def click_my_profile_button(self):
        self._form_element.find_child_element(
            Button,
            Locator.by_xpath(self.PROFILE_BUTTON),
            "Go to my profile"
        ).wait_and_click()