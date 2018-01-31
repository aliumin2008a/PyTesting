from test.common.browser import Browser


class Page(Browser):
    def __init__(self, page=None, browser_type='firefox'):
        if page:
            self.driver = page.driver
        else:
            super(Page, self).__init__(browser_type=browser_type)

    def find_element(self, *args):
        return self.driver.find_element(*args)

    def find_elements(self, *args):
        return self.get_driver().find_elements(*args)

    def open_page(self, url):
        self.get(url, maximize_windows=True)
