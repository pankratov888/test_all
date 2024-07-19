import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Настройки Chrome
options = Options()
options.add_argument("--headless")

# Инициализация веб-драйвера
service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)

try:
    print("Открытие страницы...")
    browser.get("http://ya.ru")
    print("Страница загружена.")

    # Вывод HTML страницы для отладки
    print(browser.page_source)

    # Проверка наличия элемента по атрибуту data-hydration-id
    hydration_id = "462861dcca5139608a00d9aef9841f77.0"
    WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"[data-hydration-id='{hydration_id}']")))
    print("Элемент отображается на странице.")

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    browser.quit()