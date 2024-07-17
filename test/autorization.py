import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import os
import datetime
import json
import pytest

options = webdriver.ChromeOptions()

options.add_experimental_option('detach',True)
options.add_extension(extension_path)
options.add_argument('--enable-logging')
options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
options.add_argument('--force-device-scale-factor=0.75')# Установка масштаба

# Укажите путь к вашему chromedriver
chromedriver_path = "./bin/chromedriver"
extension_path = "./bin/extensions/1.2.13_0.crx"
service = ChromeService(extension_path=chromedriver_path)
# Создайте сервис с указанием пути к chromedriver


# Создайте экземпляр браузера с использованием сервиса
driver = webdriver.Chrome(service=service, options=options)

# АВТОРИЗАЦИЯ
@allure.title("Тест авторизации через ЕСИА")
@allure.description("Проверка авторизации через ЕСИА и запись сетевых логов.")
def test_esia_auth():
    with allure.step("Открытие страницы авторизации"):
        driver.get("https://auth.pgs.gosuslugi.ru/auth/realms/DigitalgovTorkndProd1Auth/protocol/openid-connect/auth?client_id=DigitalgovTorkndProd1Auth-Proxy&state=b6fa62fc48c9м04787fa5bf095da2bafa&nonce=8bf3d529b0af28816d18e97bf560c4d3&response_type=code&redirect_uri=https%3A%2F%2Fpgs.gosuslugi.ru%2Fopenid-connect-auth%2Fredirect_uri&scope=openid")
        allure.attach(driver.get_screenshot_as_png(), name="auth_page", attachment_type=allure.attachment_type.PNG)

    with allure.step("Нажатие кнопки 'Вход через ЕСИА'"):
        esia_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='kc-social-providers']/ul")))
        esia_button.click()
        allure.attach(driver.get_screenshot_as_png(), name="esia_button_click", attachment_type=allure.attachment_type.PNG)

    driver.implicitly_wait(2)