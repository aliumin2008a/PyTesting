import threading

class ContextThread:
    def __init__(self, evn = 'test'):
        self.threadId = threading.current_thread()
        self.evn = evn
        self.data = {}

    def getContextId(self):
        return self.threadId

