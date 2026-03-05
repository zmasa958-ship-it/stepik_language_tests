import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_guest_should_see_add_to_basket_button(browser):
   
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Визуальная проверка для рецензентов (30 секунд)
    print("\nСтраница загружена.")
    time.sleep(30)
    
    # Ожидаем появления кнопки (максимум 10 секунд)
    button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket"))
    )
    
    # Проверяем, что кнопка видима
    assert button.is_displayed(), "Кнопка добавления в корзину не отображается на странице"
    
    # Проверяем, что кнопка активна
    assert button.is_enabled(), "Кнопка добавления в корзину неактивна"
    
    # Выводим текст кнопки для информации
    button_text = button.text
    print(f"\nТекст кнопки: '{button_text}'")
    
    # Основная проверка существования кнопки
    assert button, "Кнопка добавления в корзину не найдена на странице"
    
    print("Тест успешно пройден: кнопка добавления в корзину найдена")