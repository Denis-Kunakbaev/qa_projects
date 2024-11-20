from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By
from py_selenium_auto.elements.button import Button
from py_selenium_auto.elements.label import Label
from pages.forms.add_project_form import AddProjectForm


class MainPage(Form):
    AVAILABLE_PROJECTS = '//*[contains(text(), "Available projects")]'
    MAIN_CONTAINER = '//*[contains(@class, "container main-container")]'
    FOOTER = '//*[contains(@class, "footer-text")]'
    PROJECT_BUTTON = '//*[contains(text(), "{project_name}")]'
    ADD_PROJECT_BUTTON = '//*[contains(@class,"btn-xs")]'
    PROJECTS_LIST = '//*[contains(@class, "list-group")]'
    ADDED_PROJECT = '//*[contains(@class, "list-group-item") and contains(text(), "{proj_name}")]'

    def __init__(self):
        super().__init__(Locator(By.XPATH, self.MAIN_CONTAINER), 'Projects list')
        self.label_nav_header = self._element_factory.get_label(
            Locator(By.XPATH, self.AVAILABLE_PROJECTS),
            'Available projects'
        )
        self.add_project_form = AddProjectForm()

    def get_footer(self):
        return self._element_factory.get_label(
            Locator(By.XPATH, self.FOOTER),
            'Footer'
        )

    def go_to_project(self, project_name):
        self._form_element.find_child_element(
            Button,
            Locator.by_xpath(self.PROJECT_BUTTON.format(project_name=project_name)),
            "Go to nexage projects"
        ).click_and_wait()

    def add_new_project(self):
        self._form_element.find_child_element(
            Button,
            Locator.by_xpath(self.ADD_PROJECT_BUTTON),
            "Click Add project button"
        ).click_and_wait()

    def switch_to_new_tab_and_send_text(self, text):
        new_tab = self._form_element._browser.driver.window_handles[-1]
        self._form_element._browser.driver.switch_to.window(new_tab)
        self.add_project_form.send_project_name(text)

    def return_to_start_tab(self):
        start_tab = self._form_element._browser.driver.window_handles[0]
        self._form_element._browser.driver.close()
        self._form_element._browser.driver.switch_to.window(start_tab)

    def get_projects_list(self):
        return self._form_element.find_child_element(
            Label,
            Locator.by_xpath(self.PROJECTS_LIST),
            "Get projects list"
        ).text.split('\n')

    def go_to_added_project_page(self, proj_name):
        self._form_element.find_child_element(
            Button,
            Locator.by_xpath(self.ADDED_PROJECT.format(proj_name=proj_name)),
            "Go to added project page"
        ).click_and_wait()
