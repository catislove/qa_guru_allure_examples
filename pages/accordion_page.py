from selene import browser, have


class AccordionPage:

    def open_accordion_page(self):
        browser.open('/Accordion/index.html')

    def manual_testing_accordion(self):
        browser.element('#manual-testing-accordion').click()

    def check_manual_testing_accordion(self, text):
        browser.all('#manual-testing-description').element_by(have.exact_text("'{}'".format(text)))

    def сucumber_bdd_accordion(self):
        browser.element('#cucumber-accordion').click()

    def check_сucumber_bdd_accordion(self, text):
        browser.all('#cucumber-testing-description').element_by(have.exact_text("'{}'".format(text)))

    def automation_testing_accordion(self):
        browser.element('#automation-accordion').click()

    def check_automation_testing_accordion(self, text):
        browser.all('#automation-testing-description').element_by(have.exact_text("'{}'".format(text)))

    def keep_clicking_accordion(self):
        browser.element('#click-accordion').click()

    def check_keep_clicking_accordion(self, text):
        browser.all('#timeout').element_by(have.exact_text("'{}'".format(text)))

