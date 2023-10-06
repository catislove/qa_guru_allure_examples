import allure
from allure_commons.types import Severity

from pages.button_click_page import ButtonClickPage


button_click_page = ButtonClickPage()

@allure.feature('Страница с кнопками')
@allure.label('owner', 'Amalia')
@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.title('Первая кнопка')
def test_first_button():
    with allure.step("Открываем страницу c кнопками"):
        button_click_page.open_button_click_page()
    with allure.step("Нажимаем на первую кнопку"):
        button_click_page.click_first_button()
    with allure.step("Проверяем появление первого модального окна"):
        button_click_page.check_modal_window_for_first_button()
    with allure.step("Закрываем первое модальное окно"):
        button_click_page.close_modal_window_for_first_button()


@allure.feature('Страница с кнопками')
@allure.label('owner', 'Amalia')
@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.title('Вторая кнопка')
def test_second_button():
    with allure.step("Открываем страницу c кнопками"):
        button_click_page.open_button_click_page()
    with allure.step("Нажимаем на вторую кнопку"):
        button_click_page.click_second_button()
    with allure.step("Проверяем появление второго модального окна"):
        button_click_page.check_modal_window_for_second_button()
    with allure.step("Закрываем второе модальное окно"):
        button_click_page.close_modal_window_for_second_button()


@allure.feature('Страница с кнопками')
@allure.label('owner', 'Amalia')
@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.title('Третья кнопка')
def test_third_button():
    with allure.step("Открываем страницу c кнопками"):
        button_click_page.open_button_click_page()
    with allure.step("Нажимаем на третью кнопку"):
        button_click_page.click_third_button()
    with allure.step("Проверяем появление третьего модального окна"):
        button_click_page.check_modal_window_for_third_button()
    with allure.step("Закрываем третье модальное окно"):
        button_click_page.close_modal_window_for_third_button()