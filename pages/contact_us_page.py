from selene import browser, have


class ContactUsPage:

    def open_contact_page(self):
        browser.open('/Contact-Us/contactus.html')

    def enter_first_name(self, first_name):
        browser.element('[name="first_name"]').type(first_name)

    def enter_last_name(self, last_name):
        browser.element('[name="last_name"]').type(last_name)

    def enter_email(self, email):
        browser.element('[name="email"]').type(email)

    def enter_comment(self, comment):
        browser.element('[name="message"]').type(comment)

    def click_submit(self):
        browser.element('[type = "submit"]').click()

    def click_open_new_account_button(self):
        browser.element('input[type = "submit"]').click()
        browser.all('.title').element_by(have.exact_text("Congratulations, your account is now open."))

    def check(self):
        browser.all('#contact_reply').element_by(have.exact_text("Thank You for your Message!"))