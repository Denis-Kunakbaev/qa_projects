from pathlib import Path
import os

from py_selenium_auto_core.utilities.json_settings_file import JsonSettingsFile
from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper


class DataReader:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_data(self):
        root_path = RootPathHelper.calling_root_path()
        env_sub_path = str(Path(self.file_name))
        return JsonSettingsFile(env_sub_path, root_path).setting_json

    def get_photo(self):
        root_path = RootPathHelper.calling_root_path()
        env_sub_path = str(Path(self.file_name))
        return os.path.join(root_path, env_sub_path)
