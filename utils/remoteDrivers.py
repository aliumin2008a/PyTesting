import time
import threading
from utils.log import logger
data = {}
mutex = threading.Lock()
class RemoteDriver():
    def remove(self, key):
        global data
        time.sleep(1)
        if mutex.acquire(1):
            del data[key]
            logger.info(key+'对应的driver删除成功')
            mutex.release()

    def put(self, key, driver):
        global data
        time.sleep(1)
        if mutex.acquire(1):
            if key in data.keys():
                mutex.release()
                return
            lists = []
            for k in data.keys():
                lists.append(k)
            for i in range(len(lists)-20):
                try:
                    data[lists[i]].close()
                    data[lists[i]].quit()
                except Exception as ex:
                    logger.exception('webdriver操作时存在异常 %s', ex)

                del data[lists[i]]
            data[key] = driver
            mutex.release()

    def get(self, key):
        return data[key]


