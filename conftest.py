import pytest
from selenium import webdriver

def pytest_addoption(parser):
    # Добавляем параметр --language в командную строку
    parser.addoption("--language", action="store", default="en", help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    # Получаем значение параметра --language
    user_language = request.config.getoption("--language")
    
    # Настройка ChromeOptions для установки языка
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    
    # Инициализация браузера
    browser = webdriver.Chrome(options=options)
    yield browser
    
    # Закрытие браузера после теста
    browser.quit()