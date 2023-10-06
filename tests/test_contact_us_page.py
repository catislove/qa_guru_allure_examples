import allure
from allure_commons.types import Severity

from pages.contact_us_page import ContactUsPage


@allure.feature('Страница с обратной связью')
@allure.label('owner', 'Amalia')
@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.title('Заполнение и сохранение формы с обратной связью')
def test_contact_us_page():
    contact_us_page = ContactUsPage()
    with allure.step("Открываем страницу обратной связи"):
        contact_us_page.open_contact_page()
    with allure.step("Вводим фамилию"):
        contact_us_page.enter_first_name("TEST")
    with allure.step("Вводим имя"):
        contact_us_page.enter_last_name("TEST")
    with allure.step("Вводим почту"):
        contact_us_page.enter_email("TEST@mail.ru")
    with allure.step("Вводим комментарий"):
        contact_us_page.enter_comment("TEST")
    with allure.step("Нажимаем на кнопку отправки данных"):
        contact_us_page.click_submit()
    with allure.step("Проверяем, что данные отправлены"):
        contact_us_page.check()