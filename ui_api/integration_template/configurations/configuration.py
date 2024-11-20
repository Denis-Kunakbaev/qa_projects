from integration_template.configurations.environment import Environment
from constants.constants import Constants


class Configuration:

    @classmethod
    def start_url(cls):
        return Environment.current_environment(Constants.CONFIG).get("startUrl")

    @classmethod
    def api_url(cls):
        return Environment.current_environment(Constants.CONFIG).get("apiUrl")
