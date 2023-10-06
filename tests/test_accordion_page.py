import allure
from allure_commons.types import Severity

from pages.accordion_page import AccordionPage

accordion_page = AccordionPage()


@allure.feature('Страница с аккордеоном')
@allure.label('owner', 'Amalia')
@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.title('Открытие и проверка содержимого в разделе Manual Testing')
def test_manual_accordion():
    with allure.step("Открываем страницу c аккордеоном"):
        accordion_page.open_accordion_page()
    with allure.step("Расскрываем аккордеон Manual Testing"):
        accordion_page.manual_testing_accordion()
    with allure.step("Проверяем содержимое в расскрытом аккордеоне Manual Testing"):
        accordion_page.check_manual_testing_accordion('Manual testing has for some time been the most popular way to '
                                                      'test code. For this method, the tester plays an important role '
                                                      'of end user and verifies that all the features of the '
                                                      'application work correctly. Manual testing however is on the '
                                                      'decline. Companies and developers have realised the '
                                                      'efficiency, accuracy and cost savings that is possible by '
                                                      'adopting the use of automation testing.')


@allure.feature('Страница с аккордеоном')
@allure.label('owner', 'Amalia')
@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.title('Открытие и проверка содержимого в разделе Cucumber BDD')
def test_сucumber_bdd_accordion():
    with allure.step("Открываем страницу c аккордеоном"):
        accordion_page.open_accordion_page()
    with allure.step("Расскрываем аккордеон Cucumber BDD"):
        accordion_page.сucumber_bdd_accordion()
    with allure.step("Проверяем содержимое в расскрытом аккордеоне Cucumber BDD"):
        accordion_page.check_сucumber_bdd_accordion('Cucumber (BDD) simplifies the requirement capturing process. '
                                                    'Requirements can be captured, broken down and simplified '
                                                    'effortlessly; making the captured requirements readable to '
                                                    'anyone within the organisation and in turn providing the '
                                                    'required details and backbone to develop accurate test cases '
                                                    'also known as ‘Feature Files’.')


@allure.feature('Страница с аккордеоном')
@allure.label('owner', 'Amalia')
@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.title('Открытие и проверка содержимого в разделе Automation Testing')
def test_automation_accordion():
    with allure.step("Открываем страницу c аккордеоном"):
        accordion_page.open_accordion_page()
    with allure.step("Расскрываем аккордеон Automation Testing"):
        accordion_page.automation_testing_accordion()
    with allure.step("Проверяем содержимое в расскрытом аккордеоне Automation Testing"):
        accordion_page.check_automation_testing_accordion('Automation testing has been steadily grown in popularity '
                                                          'these past few years thanks to the time/ cost savings and '
                                                          'efficiency that it offers. Companies throughout the world '
                                                          'have or plan to use automation testing to rapidly speed up '
                                                          'their test capabilities. Automation test engineers are in '
                                                          'great demand and offer an average salary of £45,'
                                                          '000+ (2018). Now is a great time to learn about automation '
                                                          'test engineering and this course has been carefully '
                                                          'developed to slowly introduce you from the basics, '
                                                          'all the way to building advanced frameworks.')


@allure.feature('Страница с аккордеоном')
@allure.label('owner', 'Amalia')
@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.title('Открытие и проверка содержимого в разделе Keep Clicking')
def test_keep_clicking_accordion():
    with allure.step("Открываем страницу c аккордеоном"):
        accordion_page.open_accordion_page()
    with allure.step("Расскрываем аккордеон Keep Clicking"):
        accordion_page.keep_clicking_accordion()
    with allure.step("Проверяем содержимое в расскрытом аккордеоне Keep Clicking"):
        accordion_page.check_keep_clicking_accordion('This text has appeared after 5 seconds!')
