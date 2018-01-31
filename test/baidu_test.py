import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config, DRIVER_PATH, DATA_PATH,REPORT_PATH
from utils.log import logger
from utils.file_reader import ExcelReader
from utils.HTMLTestRunner_PY3 import HTMLTestRunner
from utils.mail import Email
from utils.screenshot import ImageUtils
from utils.alarmMessage import sendAlarm

class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    excl = DATA_PATH+'\\baidu.xlsx'
    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def su_setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        self.driver.get(self.URL)
        self.image = ImageUtils(self.driver)

    def su_tearDown(self):
        self.driver.quit()

    def test_search(self):
        datas = ExcelReader(self.excl).data
        for di in datas:
            with self.subTest(data = di):
                self.su_setUp()
                try:
                    self.driver.find_element(*self.locator_kw).send_keys(di['search'])
                    self.driver.find_element(*self.locator_su).click()
                    time.sleep(2)
                    links = self.driver.find_elements(*self.locator_result)
                    for link in links:
                        logger.info(link.text)
                    self.image.savaImage(True)
                    self.su_tearDown()
                except Exception as e:
                    self.image.savaImage(False)
                    logger.exception('元素操作出现未知异常！%s', e)
                finally:
                    if self.driver:
                        self.su_tearDown()




if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架 灰蓝', description='修改html报告')
        runner.run(TestBaiDu('test_search'))
        sendAlarm().send_message("有用例挂了快去看看吧")
    # e = Email(title='autoUITest case baidu QueryTest report',
    #           message='这是今天的报告',
    #           receiver='aliumin2008a@yeah.net',
    #           server='smtp.yeah.net',
    #           sender='aliumin2008a@yeah.net',
    #           password='18@lmOYM',
    #           path=report
    #           )
    # e.send()