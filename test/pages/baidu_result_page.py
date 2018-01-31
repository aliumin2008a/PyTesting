from selenium.webdriver.common.by import By
from test.pages.baidu_main_page import BaiDuMainPage
from test.common.page import Page


class BaiDuResultPage(Page):
    loc_result_links = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    @property
    def result_links(self):
        return self.find_elements(*self.loc_result_links)