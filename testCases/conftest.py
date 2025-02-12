import os
from datetime import datetime

import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key


@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    else:
        driver = webdriver.Chrome()
        print("Launching chrome browser.........")
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")



########### pytest HTML Report ################


def pytest_configure(config):
    # Use config.stash to add metadata for pytest-metadata plugin
    if hasattr(config, 'pluginmanager'):
        metadata_plugin = config.pluginmanager.getplugin("metadata")
        if metadata_plugin:
            config.stash[metadata_key]['Project Name'] = 'Zodiac'
            config.stash[metadata_key]['Module Name'] = 'User Login'
            config.stash[metadata_key]['Tester Name'] = 'Vivek Devkar'

    # Specify report folder location and save report with timestamp
    report_dir = os.path.join(os.path.abspath(os.curdir), "reports")
    os.makedirs(report_dir, exist_ok=True)  # Create the reports directory if it doesn't exist
    config.option.htmlpath = os.path.join(report_dir, f"{datetime.now().strftime('%d-%m-%Y %H-%M-%S')}.html")


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    # Remove specific metadata entries from the report
    metadata.pop("Python", None)
    metadata.pop("Plugins", None)





# ------------------------------------------------------------------------

# Headless mode

# import pytest
# import os
# from pytest_metadata.plugin import metadata_key
# from datetime import datetime
# import configparser
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver.edge.options import Options as EdgeOptions
#
# # Load config.ini
# config = configparser.ConfigParser()
# config.read(os.path.join(os.path.abspath(os.curdir), 'configurations', 'config.ini'))
#
# def pytest_addoption(parser):
#     """Command-line options for pytest"""
#     parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome, firefox, edge")
#     parser.addoption("--headless", action="store_true", help="Run browser in headless mode")
#
# @pytest.fixture()
# def setup(request):
#     """Setup WebDriver based on provided browser and headless option"""
#     browser = request.config.getoption("--browser")
#     headless = request.config.getoption("--headless")
#
#     if browser == "chrome":
#         options = ChromeOptions()
#         if headless:
#             options.add_argument("--headless=new")  # Use --headless=new for newer versions
#             options.add_argument("--disable-gpu")
#             options.add_argument("--window-size=1920,1080")
#         driver = webdriver.Chrome(options=options)
#
#     elif browser == "firefox":
#         options = FirefoxOptions()
#         if headless:
#             options.add_argument("--headless")
#         driver = webdriver.Firefox(options=options)
#
#     elif browser == "edge":
#         options = EdgeOptions()
#         if headless:
#             options.add_argument("--headless")
#             options.add_argument("--disable-gpu")
#         driver = webdriver.Edge(options=options)
#
#     else:
#         raise ValueError(f"Unsupported browser: {browser}")
#
#     request.cls.driver = driver
#     driver.get(config.get('commonInfo', 'baseURL'))
#     driver.maximize_window()
#     yield driver
#     driver.quit()
#
# @pytest.fixture()
# def browser(request):
#     """Return browser name"""
#     return request.config.getoption("--browser")
#
# def pytest_configure(config):
#     """Configure test report and metadata"""
#     if hasattr(config, 'pluginmanager'):
#         metadata_plugin = config.pluginmanager.getplugin("metadata")
#         if metadata_plugin:
#             config.stash[metadata_key]['Project Name'] = 'Zodiac'
#             config.stash[metadata_key]['Module Name'] = 'User Registration'
#             config.stash[metadata_key]['Tester Name'] = 'Vivek Devkar'
#
#     report_dir = os.path.join(os.path.abspath(os.curdir), "reports")
#     os.makedirs(report_dir, exist_ok=True)
#     config.option.htmlpath = os.path.join(report_dir, f"{datetime.now().strftime('%d-%m-%Y %H-%M-%S')}.html")
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     """Customize test report metadata"""
#     metadata.pop("Python", None)
#     metadata.pop("Plugins", None)
