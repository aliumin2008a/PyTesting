from selenium.webdriver.common.by import By
from test.common.basePage import BasePage

class AlipayLogin(BasePage):
    loc_search_input = (By.ID, 'kw')
    loc_search_button = (By.ID, 'su')

    def search(self, kw, url):
        """搜索功能"""
        self.openPage(url)
        self.find_element(*self.loc_search_input).send_keys(kw)
        self.find_element(*self.loc_search_button).click()

    def openPage(self, url):
        self.get(url)