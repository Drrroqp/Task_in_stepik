import time
import pytest
from selenium.webdriver.common.by import By

def test_button_add_to_basket_is_visible(browser):
    # URL страницы товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    
    # Открываем страницу
    browser.get(link)
    
    # Добавляем паузу для визуальной проверки (удалить или закомментировать после проверки)
    time.sleep(30)
    
    # Проверяем наличие кнопки добавления в корзину
    button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(button) > 0, "Кнопка добавления в корзину не найдена!"