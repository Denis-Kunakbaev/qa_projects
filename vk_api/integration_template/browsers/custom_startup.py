from typing import Optional, Callable

from py_selenium_auto.browsers.browser_startup import BrowserStartup, BrowserServiceProvider
from py_selenium_auto_core.utilities.json_settings_file import JsonSettingsFile
from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper
import os


class CustomStartup(BrowserStartup):

    @classmethod
    def configure_services(
            cls,
            application_provider: Callable,
            settings: Optional[JsonSettingsFile] = None,
            service_provider: BrowserServiceProvider = None,
    ) -> BrowserServiceProvider:
        settings = settings or cls.get_settings(
            RootPathHelper.calling_root_path(),
            os.path.join(RootPathHelper.current_root_path(__file__), "integration_template"),
        )

        service_provider = super().configure_services(application_provider, settings, service_provider)
        return service_provider
