from dataclasses import dataclass


@dataclass
class WallPostParams:
    message: str


@dataclass
class WallEditParams:
    post_id: int
    message: str
    attachments: str = None


@dataclass
class SaveWallPhotoParams:
    v: str
    access_token: str
    photo: str
    server: int
    hash: str


@dataclass
class WallCreateCommentParams:
    post_id: int
    message: str


@dataclass
class WallGetLikesParams:
    item_id: int
    type: str = 'post'


@dataclass
class WallDeleteParams:
    post_id: int
