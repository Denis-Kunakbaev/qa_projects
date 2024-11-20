import dataclasses

from vk_api.api_utils.request_manager import RequestManager
from tests.test_utils.data_reader import DataReader
from constants.file_names import FileNames
from models.config_model import ConfigModel
from integration_template.configurations.configuration import Configuration
from vk_api.api_utils.file_loader import FileLoader
from constants.endpoints import Endpoints
from models.response_models import *
from models.request_models import *


class RequestUtil:

    def __init__(self):
        self.request_manager = RequestManager(Configuration.api_url())
        self.methods = Endpoints()
        self.api_config = ConfigModel.from_dict(DataReader(FileNames.CONFIG).get_data())
        self.file_loader = FileLoader()
        self._server = None
        self._photo = None
        self._hash = None
        self._photo_id = None

    def _make_request(self, method, **kwargs):
        params = {'v': self.api_config.version,
                  'access_token': self.api_config.token,
                  **kwargs}
        response = self.request_manager.send_get_request(method, params=params)
        return response

    def get_user_id(self):
        response = self._make_request(
            self.methods.USERS_GET,
        )
        user_id = ResponseUser.from_json(response.text).response[0].id
        return user_id

    def create_post_wall(self, text):
        params = WallPostParams(message=text)
        params_dict = dataclasses.asdict(params)
        response = self._make_request(
            self.methods.WALL_POST,
            **params_dict
        )
        return response

    def edit_post(self, user_id, post_id, message):
        self._photo_id = self.get_photo_id()
        params = WallEditParams(post_id=post_id, message=message,
                                attachments=f"photo{user_id}_{self._photo_id}")
        params_dict = dataclasses.asdict(params)
        self._make_request(
            self.methods.WALL_EDIT,
            **params_dict
        )

    def get_photo_id(self):
        upload_server_url = self.get_wall_photo_upload_server()
        self.upload_photo_to_server(upload_server_url, DataReader(FileNames.UPLOADED_FILE).get_photo())
        return self.upload_wall_photo()

    def get_wall_photo_upload_server(self) -> str:
        response = self._make_request(self.methods.GET_PHOTO_SERVER)
        upload_server_model = ResponseWallUploadServer.from_json(response.text)
        return upload_server_model.response.upload_url

    def upload_photo_to_server(self, url, file_path):
        with open(file_path, 'rb') as photo_file:
            response = self.request_manager.send_post_request(taken_url=url,
                                                              files={'photo': photo_file}
                                                              )

        data = ServerInfoModel.from_json(response.text)
        self._server = data.server
        self._photo = data.photo
        self._hash = data.hash

    def upload_wall_photo(self):
        params = SaveWallPhotoParams(v=self.api_config.version,
                                     access_token=self.api_config.token,
                                     photo=self._photo,
                                     server=self._server,
                                     hash=self._hash)
        params_dict = dataclasses.asdict(params)
        response = self.request_manager.send_post_request(
            self.methods.SAVE_WALL_PHOTO,
            params=params_dict,
        )

        return PhotoInfoModel.from_json(response.text).response[0].id

    def create_comment(self, post_id, message):
        params = WallCreateCommentParams(post_id=post_id, message=message)
        params_dict = dataclasses.asdict(params)
        self._make_request(
            self.methods.WALL_CREATE_COMMENT,
            **params_dict
        )

    def get_likes(self, post_id):
        params = WallGetLikesParams(item_id=post_id)
        params_dict = dataclasses.asdict(params)
        response = self._make_request(
            self.methods.WALL_GET_LIKES,
            **params_dict
        )
        return response

    def delete_wall(self, post_id):
        params = WallDeleteParams(post_id=post_id)
        params_dict = dataclasses.asdict(params)
        self._make_request(
            self.methods.WALL_DELETE,
            **params_dict
        )
