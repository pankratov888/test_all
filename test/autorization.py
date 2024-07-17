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
options.add_argument("--headless")

# Инициализация веб-драйвера с использованием ChromeDriverManager
service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)

try:
    print("Открытие страницы...")
    browser.get("http://ya.ru")
    print("Страница загружена.")

    # Проверка наличия элемента
    element_xpath = "/html/body/main/div[3]/form/div[3]/div/div[1]"
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, element_xpath)))
    print("Элемент отображается на странице.")

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    # Закрытие драйвера
    browser.quit()