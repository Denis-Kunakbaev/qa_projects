import allure
from tests.test_base import TestBase
from pages.autorization_page import AutorizationPage
from pages.login_page import LoginPage
from pages.news_page import NewsPage
from pages.profile_page import ProfilePage
from models.response_models import *
from tests.test_utils.data_reader import DataReader
from models.config_model import ConfigModel
from constants.file_names import FileNames
from vk_api.api_utils.api_utils import RequestUtil
from vk_api.api_utils.file_loader import FileLoader
from vk_api.api_utils.file_comparator import FileComparator
from tests.test_utils.random_text_generator import RandomTextGenerator


class TestVk(TestBase):
    config = ConfigModel.from_dict(DataReader(FileNames.CONFIG).get_data())
    autorization_page = AutorizationPage()
    login_page = LoginPage()
    news_page = NewsPage()
    profile_page = ProfilePage()
    api_utils = RequestUtil()
    file_loader = FileLoader()
    file_comparator = FileComparator()


    def setup(self):
        with allure.step("Go to login page"):
            self.go_to_start_page()

        with allure.step("Login page is displayed"):
            assert self.login_page.state.is_displayed(), 'The login page was not opened'
            assert self.login_page.label_nav_header.state.wait_for_displayed(), 'The header of login page was not opened'

    def test_vk(self):
        with allure.step('Send email to text field'):
            self.login_page.send_email_to_text_field(self.config.email)
            self.login_page.click_signin_button()

        # This method is used when it's necessary to change the authorization type.
        #  You should uncomment this block of code if an authorization window appears that requires an access code.
        # with allure.step('Change autorization method'):
        #     assert self.autorization_page.state.wait_for_displayed(), 'The autorization page was not opened'
        #     self.autorization_page.click_change_autorization_method_button()
        #     self.autorization_page.verification_form.click_password_method_button()

        with allure.step('Send password to text field'):
            assert self.autorization_page.state.wait_for_displayed(), 'The autorization page was not opened'
            self.autorization_page.send_password_to_text_field(self.config.password)
            self.autorization_page.click_submit_button()

        with allure.step('News page is displayed'):
            assert self.news_page.label_nav_header.state.wait_for_displayed(), 'The news page was not opened'

        with allure.step('Go to my profile page'):
            self.news_page.click_my_profile_button()

        post_id = None
        user_id = None

        with allure.step('Create post'):
            post_text = RandomTextGenerator.get_random_text(message_length=10)
            post = ResponsePost.from_json(self.api_utils.create_post_wall(post_text).text)
            post_id = post.response.post_id
            assert isinstance(post_id, int), 'Post id is not integer'
            user_id = self.api_utils.get_user_id()
            wall_post = self.profile_page.get_post_by_id(user_id, post_id)
            assert self.config.user_name in wall_post, f'Post was not created by {self.config.user_name}'
            assert post_text in wall_post, f'Post does not contain text :{post_text}'

        with allure.step('Edit post'):
            new_text = RandomTextGenerator.get_random_text(message_length=10)
            self.api_utils.edit_post(user_id, post_id, new_text)
            photo_id = self.api_utils._photo_id
            assert self.profile_page.wait_for_post_edited(user_id, post_id,
                                                          post_text), 'Post was not edited'
            photo_link = self.profile_page.get_photo_url(user_id, photo_id)
            self.file_loader.download_file(FileNames.DOWNLOADED_FILE, photo_link)
            assert self.file_comparator.compare_images(FileNames.DOWNLOADED_FILE, FileNames.UPLOADED_FILE), \
                'Images are not similar'

        with allure.step('Comment post'):
            comment = RandomTextGenerator.get_random_text(message_length=10)
            self.api_utils.create_comment(post_id, comment)
            assert self.profile_page.wait_for_comment_added(user_id, post_id, comment), \
                f'Comment {comment} was not added to post {post_id}'
            wall_post = self.profile_page.get_post_by_id(user_id, post_id)
            assert self.config.user_name in wall_post and comment in wall_post, \
                f'Comment {comment} was not created by {self.config.user_name}'

        with allure.step('React post'):
            self.profile_page.click_reaction_button(user_id, post_id)
            likes_response = self.api_utils.get_likes(post_id)
            liked = ResponseLikes.from_json(likes_response.text).response.liked
            assert bool(liked), f'Like by user {user_id} was not created'

        with allure.step('Delete post'):
            self.api_utils.delete_wall(post_id)
            assert self.profile_page.check_deleted_post(user_id, post_id) \
                , 'Post was not deleted'
