
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import allure


@allure.epic("Мобильное приложение")
@allure.story("Поиск и клик по календарю в списке")
@allure.title("Тест поиска элемента 'Calendar' скроллом")
@allure.severity(allure.severity_level.NORMAL)
def test_calendar_finding(android_driver:WebDriver, wait: WebDriverWait) -> None:
    with allure.step("Клик по стартовому приложению 'PNW'"):
        element = wait.until(
            EC.visibility_of_element_located((AppiumBy.XPATH,
                                                '//android.widget.TextView[@content-desc="Predicted app: Package Names"]')))
        element.click()
    last_elements = []
    scroll_count = 0
    while True:
        scroll_count += 1
        with allure.step(f"Итерация скролла №{scroll_count}."):
            elements = wait.until(
                EC.presence_of_all_elements_located((AppiumBy.ID, "com.csdroid.pkg:id/tv_title")))
            android_driver.swipe(elements[1].rect['x'], elements[1].rect['y'], elements[0].rect['x'], elements[0].rect['y'])
        elements = wait.until(
            EC.presence_of_all_elements_located((AppiumBy.ID, "com.csdroid.pkg:id/tv_title")))
        with allure.step("Проверка наличия элемента 'Calendar'"):
            element_names = [name.text for name in elements]
            if 'Calendar' in element_names:
                with allure.step("Элемент 'Calendar' найден. Кликаем по нему"):
                    elements[element_names.index('Calendar')].click()
                break
        with allure.step("Проверка: достигнут ли конец списка?"):
            if elements == last_elements:
                raise NoSuchElementException("Нет календаря в данном списке")
        last_elements = elements
    with allure.step("Финальная проверка успешности выполнения теста"):
        assert True