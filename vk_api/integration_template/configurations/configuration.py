from integration_template.configurations.environment import Environment
from constants.file_names import FileNames


class Configuration:

    @classmethod
    def start_url(cls):
        return Environment.current_environment(FileNames.CONFIG).get("startUrl")

    @classmethod
    def api_url(cls):
        return Environment.current_environment(FileNames.CONFIG).get("apiUrl")
