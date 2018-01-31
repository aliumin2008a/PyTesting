from test.common.browser import Browser

class BasePage(Browser):
    def find_element(self, *args):
        return self.get_driver().find_element(*args)

    def find_elements(self, *args):
        return self.get_driver().find_elements(*args)

    def open_page(self, url):
        self.get(url, maximize_windows=True)