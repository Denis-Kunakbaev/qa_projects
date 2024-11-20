import logging
import os

import pytest
from _pytest.fixtures import FixtureRequest
from py_selenium_auto.browsers.browser_services import BrowserServices

from py_selenium_auto_core.logging.logger import Logger
from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper

from integration_template.browsers.custom_startup import CustomStartup


@pytest.fixture(scope="session", autouse=True)
def setup_session(request):

    work_dir = RootPathHelper.calling_root_path()
    os.chdir(work_dir)
    Logger.info(f'Setting work_dir: {work_dir}')

    for log_name in [
        "selenium.webdriver.remote.remote_connection",
        "selenium.webdriver.common.selenium_manager",
        "urllib3.connectionpool",
    ]:
        logger = logging.getLogger(log_name)
        logger.disabled = True

    config_path = os.path.join(work_dir, "resources", "config.json")
    Logger.info(f"Loading config from: {config_path}")

    Logger.info("Setup startup config")
    BrowserServices.Instance.set_startup(CustomStartup())
    yield


@pytest.fixture(scope="function", autouse=True)
def setup_function(request: FixtureRequest):
    BrowserServices.Instance.browser.maximize()
    yield
    if BrowserServices.Instance.is_browser_started:
        Logger.info("Closing browser")
        BrowserServices.Instance.browser.quit()


