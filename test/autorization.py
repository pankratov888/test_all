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
# Пример: открыть браузер в режиме без головы (без графического интерфейса)
#options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1024x768')
options.add_argument('--ssl-version-min=tls1.2')


# Путь к расширению
extension_path = './extensions/1.2.13_0.crx'
options.add_extension(extension_path)


# Инициализация веб-драйвера с использованием ChromeDriverManager
service = ChromeService('./bin/chromedriver')
browser = webdriver.Chrome(service=service, options=options)

try:
    print("Открытие страницы...")
    browser.get("https://ya.ru/")
    print("Страница загружена.")

    # Вывод HTML страницы для отладки
    print(browser.page_source)
    time.sleep(5)
    # Проверка наличия элемента по id
    element_id = "fe63b914944963d357284f633f943e18.0"
    WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.ID, element_id)))
    print("Элемент отображается на странице.")

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    browser.quit()