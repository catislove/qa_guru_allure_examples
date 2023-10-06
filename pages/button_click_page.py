from selene import browser, have, by


class ButtonClickPage:

    def open_button_click_page(self):
        browser.open('/Click-Buttons/index.html')

    def click_first_button(self):
        browser.element('#button1').click()

    def check_modal_window_for_first_button(self):
        browser.all('h4').element_by(have.exact_text("Congratulations!"))

    def close_modal_window_for_first_button(self):
        browser.element(by.xpath('//div[@id="myModalClick"]//button[contains(text(), "Close")]')).click()

    def click_second_button(self):
        browser.element('#button2').click()

    def check_modal_window_for_second_button(self):
        browser.all('h4').element_by(have.exact_text("It’s that Easy!!  Well I think it is....."))

    def close_modal_window_for_second_button(self):
        browser.element(by.xpath('//div[@id="myModalJSClick"]//button[contains(text(), "Close")]')).click()

    def click_third_button(self):
        browser.element('#button3').click()

    def check_modal_window_for_third_button(self):
        browser.all('h4').element_by(have.exact_text("Well done! the "))

    def close_modal_window_for_third_button(self):
        browser.element(by.xpath('//div[@id="myModalMoveClick"]//button[contains(text(), "Close")]')).click()