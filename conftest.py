import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    #Добавляем обработчик параметра language в командной строке
    parser.addoption(
        '--language', 
        action='store', 
        default='en',
        help="Choose language: en, ru, fr, es, etc."
    )

@pytest.fixture(scope="function")
def browser(request):
    # Получаем язык из командной строки
    user_language = request.config.getoption("language")
    
    print(f"\nЗапускаем Chrome с языком: {user_language}")
    
    # Настройка языка для Chrome
    options = Options()
    options.add_experimental_option(
        'prefs', 
        {'intl.accept_languages': user_language}
    )
    
    # Создаем экземпляр браузера
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    
    # Возвращаем браузер в тест
    yield browser
    
    # Закрываем браузер после теста
    print("\nЗакрываем браузер...")
    browser.quit()