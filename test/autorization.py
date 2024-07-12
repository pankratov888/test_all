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

# Укажите путь к исполняемому файлу Chrome-Gost
chrome_gost_path = "C:\\Users\\pankr\\AppData\\Local\\Chromium\\Application\\chrome.exe"  # Убедитесь, что путь правильный
# Определите путь к расширению
extension_path = os.path.join(os.path.dirname(__file__), '../extensions/1.2.13_0.crx')  # Замените на ваше имя расширения
binary_yandex_driver_file = os.path.join(os.path.dirname(__file__), '../bin/chromedriver.exe')

options = webdriver.ChromeOptions()

options.add_experimental_option('detach',True)
options.add_extension(extension_path)
options.add_argument('--enable-logging')
options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
options.add_argument('--force-device-scale-factor=0.75')# Установка масштаба
service = ChromeService(executable_path=binary_yandex_driver_file)
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10)
driver.maximize_window()



driver.get("https://ya.ru")
time.sleep(4)
driver.quit()

