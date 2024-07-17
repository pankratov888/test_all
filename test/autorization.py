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

# Путь к расширению
extension_path = './extensions/1.2.13_0.crx'
options.add_extension(extension_path)

# Инициализация веб-драйвера с использованием ChromeDriverManager
service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)

try:
    print("Открытие страницы...")
    browser.get("https://auth.pgs.gosuslugi.ru/auth/realms/DigitalgovTorkndProd1Auth/protocol/openid-connect/auth?client_id=DigitalgovTorkndProd1Auth-Proxy&state=b6fa62fc48c9м04787fa5bf095da2bafa&nonce=8bf3d529b0af28816d18e97bf560c4d3&response_type=code&redirect_uri=https%3A%2F%2Fpgs.gosuslugi.ru%2Fopenid-connect-auth%2Fredirect_uri&scope=openid")
    print("Страница загружена.")

    # Вывод HTML страницы для отладки
    print(browser.page_source)

    # Проверка наличия элемента по id
    element_id = "zocial-esia"
    WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.ID, element_id)))
    print("Элемент отображается на странице.")

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    browser.quit()