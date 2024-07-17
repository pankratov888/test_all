from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Настройка опций Chrome
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--remote-debugging-port=9222')

# Установка ChromeDriver
service = ChromeService(executable_path=ChromeDriverManager().install())

# Инициализация веб-драйвера
driver = webdriver.Chrome(service=service, options=chrome_options)

# Ваш тестовый код
driver.get("http://example.com")
print(driver.title)

# Закрытие драйвера
driver.quit()
