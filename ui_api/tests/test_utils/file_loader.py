import base64
import os

from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper
from constants.constants import Constants


class FileLoader:
    @staticmethod
    def download_image(link):
        _, base64_data = link.split(',', 1)
        img_data = base64.b64decode(base64_data)
        root_path = RootPathHelper._find_root_path(os.getcwd())
        downloaded_image = os.path.join(root_path, Constants.DOWNLOADED_IMAGE)
        with open(downloaded_image, 'wb') as f:
            f.write(img_data)
