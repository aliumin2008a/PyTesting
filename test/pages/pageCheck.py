from selenium.webdriver.common.by import By
from test.common.page import Page

class PageCheck(Page):
    loc_result_links = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    @property
    def result_links(self):
        return self.find_elements(*self.loc_result_links)
