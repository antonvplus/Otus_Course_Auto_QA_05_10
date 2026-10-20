from collections.abc import Generator

import pytest
from appium import webdriver
from appium.options.common import AppiumOptions
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

import allure

APPIUM_SERVER_URL = "http://127.0.0.1:4723"

@pytest.fixture()
def android_driver() -> Generator[WebDriver, None, None]:
    with allure.step("Инициализация Appium драйвера и запуск приложения"):
        options = AppiumOptions()
        options.load_capabilities({
            "appium:deviceName": "Pixel_10_Pro",
            "platformName": "Android",
            "appium:automationName": "UiAutomator2"})
        android_driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)
    yield android_driver
    with allure.step("Закрытие сессии Appium драйвера"):
        android_driver.quit()

@pytest.fixture()
def wait(android_driver: WebDriver) -> WebDriverWait:
    return WebDriverWait(android_driver, 10)
