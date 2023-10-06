from selene import browser, have, by


class ToDoListPage:

    def open_to_do_list_page(self):
        browser.open('/To-Do-List/index.html')

    def add_and_check_new_todo(self, todo):
        browser.element('[placeholder="Add new todo"]').type(todo).press_enter()
        browser.all('li').element_by(have.exact_text(todo))

    def completed_todo(self, completed_todo):
        browser.element(by.xpath("//li[contains(text(), '{}')]".format(completed_todo))).click()
        browser.all('.completed').element_by(have.exact_text(completed_todo))
