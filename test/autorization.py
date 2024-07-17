from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Укажите путь к вашему chromedriver
chromedriver_path = "./bin/chromedriver"

# Создайте сервис с указанием пути к chromedriver
service = Service(chromedriver_path)

# Создайте экземпляр браузера с использованием сервиса
driver = webdriver.Chrome(service=service)

driver.get("http://example.com")
print(driver.title)
driver.quit()