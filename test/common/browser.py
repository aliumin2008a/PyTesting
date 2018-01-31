import time
import os
from utils.config import DRIVER_PATH, REPORT_PATH ,IMAGE_PATH
from utils.contextThread import ContextThread
from utils.remoteDrivers import RemoteDriver
from selenium import webdriver
# 可根据需要自行扩展
CHROMEDRIVER_PATH = DRIVER_PATH + '\chromedriver.exe'
IEDRIVER_PATH = DRIVER_PATH + '\IEDriverServer.exe'
PHANTOMJSDRIVER_PATH = DRIVER_PATH + '\phantomjs.exe'

TYPES = {'firefox': webdriver.Firefox, 'chrome': webdriver.Chrome, 'ie': webdriver.Ie, 'phantomjs': webdriver.PhantomJS}
EXECUTABLE_PATH = {'firefox': 'wires', 'chrome': CHROMEDRIVER_PATH, 'ie': IEDRIVER_PATH, 'phantomjs': PHANTOMJSDRIVER_PATH}
class UnSupportBrowserTypeError(Exception):
    pass

class Browser(object):
    def __init__(self, browser_type='firefox'):
        self._type = browser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise UnSupportBrowserTypeError('暂时仅支持%s' % ','.join(TYPES.keys()))
        self.driver = None
        self.cont = ContextThread()
        self.remote = RemoteDriver()

    def get(self, url, maximize_windows = True, implicitly_wait=30):
        self.driver = self.browser(executable_path=EXECUTABLE_PATH[self._type])
        self.remote.put(self.cont.getContextId(), self.driver)
        self.driver.get(url)
        if maximize_windows:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        return self

    def save_screen_shot(self, name = 'screen_shot'):
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        screenshot_path = IMAGE_PATH + '\screenshot_%s' % day
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        tm = time.strftime('%H%M%S', time.localtime(time.time()))
        screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.png' % (name, tm))
        return screenshot

    def get_driver(self):
        if self.driver is not None:
            return self.driver
        else:
            return self.remote.get(self.cont.getContextId())

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()