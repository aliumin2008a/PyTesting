import requests ,json, datetime, time
from utils.config import Config

class sendAlarm:
    def __init__(self):
        self.webhook = Config().get("WEBHOOK")
        self.persons = Config().get("ATPERSON")

    def send_message(self, content):
        pagrem = {
            "msgtype": "text",
            "text": {
                "content": content
                },
            "at": {
                "atMobiles": self.persons
            },
            "isAtAll": True
        }
        headers = {"Content-Type": "application/json"}
        requests.post(self.webhook, data=json.dumps(pagrem), headers=headers)

