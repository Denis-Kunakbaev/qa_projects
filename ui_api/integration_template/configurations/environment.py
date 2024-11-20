from pathlib import Path

from py_selenium_auto_core.utilities.json_settings_file import JsonSettingsFile
from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper


class Environment:

    @staticmethod
    def current_environment(file_name):
        root_path = RootPathHelper.calling_root_path()
        env_sub_path = str(Path(file_name))
        return JsonSettingsFile(env_sub_path, root_path)
