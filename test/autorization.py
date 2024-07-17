from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Настройки Chrome
options = Options()
# Пример: открыть браузер в режиме без головы (без графического интерфейса)
options.add_argument("--headless")

# Инициализация веб-драйвера с использованием ChromeDriverManager
service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)

print("Открытие страницы...")
browser.get("http://ya.ru")
print("Страница загружена.")


# Закрытие драйвера
browser.quit()
