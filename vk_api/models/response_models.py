from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin
from typing import List


@dataclass
class LikesInfo(DataClassJsonMixin):
    liked: int
    copied: int
    reaction_id: int


@dataclass
class ResponseLikes(DataClassJsonMixin):
    response: LikesInfo


@dataclass
class WallPostInfo(DataClassJsonMixin):
    post_id: int = None


@dataclass
class UserInfoResponse:
    id: int = None
    first_name: str = None
    last_name: str = None
    can_access_closed: bool = None
    is_closed: bool = None


@dataclass
class ResponseUser(DataClassJsonMixin):
    response: List[UserInfoResponse]


@dataclass
class ResponsePost(DataClassJsonMixin):
    response: WallPostInfo


@dataclass
class WallUploadServerModel(DataClassJsonMixin):
    album_id: int = None
    upload_url: str = None
    user_id: int = None


@dataclass
class ResponseWallUploadServer(DataClassJsonMixin):
    response: WallUploadServerModel


@dataclass
class ServerInfoModel(DataClassJsonMixin):
    server: int
    photo: str
    hash: str


@dataclass
class OrigPhoto:
    height: int
    type: str
    url: str
    width: int


@dataclass
class PhotoParams:
    album_id: int
    date: int
    id: int
    owner_id: int
    access_key: str
    sizes: List[OrigPhoto]
    text: str
    web_view_token: str
    has_tags: bool
    orig_photo: OrigPhoto


@dataclass
class PhotoInfoModel(DataClassJsonMixin):
    response: List[PhotoParams]
