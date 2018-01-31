import time
import unittest
from utils.config import Config, DATA_PATH, REPORT_PATH
from utils.log import logger
from utils.file_reader import ExcelReader
from utils.HTMLTestRunner_PY3 import HTMLTestRunner
from utils.mail import Email
from test.pages.baidu_result_page import BaiDuResultPage, BaiDuMainPage
from utils.alarmMessage import sendAlarm

class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/baidu.xlsx'

    def sub_setUp(self):
        self.page = BaiDuMainPage(browser_type='chrome').get(self.URL, maximize_windows=True)

    def sub_tearDown(self):
        self.page.quit()

    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.page.search(d['search'])
                self.page.save_screen_shot(d['search'])
                time.sleep(2)
                self.page = BaiDuResultPage(self.page)
                self.page.save_screen_shot(d['search']+'_result')
                links = self.page.result_links
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()

if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架 灰蓝', description='修改html报告')
        runner.run(TestBaiDu('test_search'))
    #     sendAlarm().send_message("有用例挂了快去看看吧")
    # e = Email(title='autoUITest case baidu QueryTest report',
    #           message='这是今天的报告',
    #           receiver='aliumin2008a@yeah.net',
    #           server='smtp.yeah.net',
    #           sender='aliumin2008a@yeah.net',
    #           password='18@lmOYM',
    #           path=report
    #           )
    # e.send()