from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Установка ChromeDriver
service = ChromeService(executable_path=ChromeDriverManager().install())

# Инициализация веб-драйвера
driver = webdriver.Chrome(service=service)

# Ваш тестовый код
driver.get("http://ya.ru")
print(driver.title)

# Закрытие драйвера
driver.quit()