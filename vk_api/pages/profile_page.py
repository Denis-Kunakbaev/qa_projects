from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By
from py_selenium_auto.elements.label import Label
from py_selenium_auto.elements.link import Link


class ProfilePage(Form):
    PROFILE_WALL_ID = 'profile_wall'
    PHOTO_URL_XPATH_TEMPLATE =\
        '//*[contains(@href,"{user_id}_{photo_id}")]//*[contains(@class , "PhotoPrimaryAttachment__imageElement")]'
    REACTION_BUTTON_XPATH_TEMPLATE =\
        '//*[contains(@id, "post{user_id}_{post_id}")]//*[contains(@class, "PostBottomActionContainer")]'
    POST_TEXT_XPATH_TEMPLATE =\
        '//*[contains(@id, "post{user_id}_{post_id}")]//*[contains(@class, "wall_post_text") and contains(text(), "{text}")]'
    COMMENT_TEXT_XPATH_TEMPLATE =\
        '//*[contains(@id, "post{user_id}_{post_id}")]//*[contains(@class, "wall_reply_text onclick") and contains(text(), "{comment}")]'
    POST_XPATH_TEMPLATE = 'post{user_id}_{post_id}'

    def __init__(self):
        super().__init__(Locator(By.ID, self.PROFILE_WALL_ID), 'Profile')

    def get_post_by_id(self, user_id, post_id):
        post = self._form_element.find_child_element(
            Label,
            Locator.by_id(self.POST_XPATH_TEMPLATE.format(user_id=user_id, post_id=post_id)),
            "Get post"
        )
        return post.text

    def get_photo_url(self, user_id, photo_id):
        img = self._form_element.find_child_element(
            Link,
            Locator.by_xpath(
                self.PHOTO_URL_XPATH_TEMPLATE.format(user_id=user_id, photo_id=photo_id)),
            "Get post photo url"
        )
        link = img.get_attribute('src')
        return link

    def click_reaction_button(self, user_id, post_id):
        self._form_element.find_child_element(
            Label,
            Locator.by_xpath(
                self.REACTION_BUTTON_XPATH_TEMPLATE.format(user_id=user_id, photo_id=post_id)),
            'Get reaction info'
        ).click()

    def wait_for_post_edited(self, user_id, post_id, text):
        return self._form_element.find_child_element(
            Label,
            Locator.by_xpath(
                self.POST_TEXT_XPATH_TEMPLATE.format(user_id=user_id, post_id=post_id, text=text)),
            'Wait for post edited').state.wait_for_not_displayed()

    def wait_for_comment_added(self, user_id, post_id, comment):
        return self._form_element.find_child_element(
            Label,
            Locator.by_xpath(
                self.COMMENT_TEXT_XPATH_TEMPLATE.format(user_id=user_id, post_id=post_id, comment=comment)),
            'Get reaction info').state.wait_for_displayed()

    def check_deleted_post(self, user_id, post_id):
        return self._element_factory.get_label(
            Locator(By.XPATH, self.POST_XPATH_TEMPLATE.format(user_id=user_id, post_id=post_id)),
            'Deleted post'
        ).state.wait_for_not_displayed()
