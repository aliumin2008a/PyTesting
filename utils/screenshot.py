import os,sys,time
from utils.config import IMAGE_PATH

class ImageUtils:
    def __init__(self, webDriver, isScreenshot=True):
        self.isScreenshot = isScreenshot
        self.webDriver = webDriver

    def savaImage(self, isException):
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        if isException:
            pic_path = IMAGE_PATH + '\\'+current_time +'_success.png'
        else:
            pic_path = IMAGE_PATH +'\\'+ current_time+'_Failuer.png'

        self.webDriver.get_screenshot_as_file(pic_path)
