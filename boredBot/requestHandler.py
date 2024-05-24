import requests
import json
from secret import botToken

class rh:
    def __init__(self):
        self.TGurl = f"https://api.telegram.org/bot{botToken}/"
        self.boredurl = "https://www.boredapi.com/api/activity/"

    
    def getUpdates(self, offset = 0):
        requestUrl = self.TGurl + "getUpdates" + "?offset=" + str(offset)
        r = requests.get(requestUrl)
        if r.status_code == 200:
            data = r.json()
            return data
        else:
            return None
        
    def checkForNewMessages(self, offset):
        requestUrl = self.TGurl + "getUpdates" + "?offset=" + str(offset)
        r = requests.get(requestUrl)
        if r.status_code == 200:
            data = r.json()
            if data['ok'] == False:
                return False
            else:
                if len(data['result']) > 0:
                    return True
                else:
                    return False
        else:
            return None
    
    def sendMessage(self, chat_id, text, additionalParams = None):
        if additionalParams == None:
            additionalParams = ""
        else:
            additionalParams = "&" + additionalParams
        requestUrl = self.TGurl + "sendMessage?chat_id=" + str(chat_id) + "&text=" + text + str(additionalParams)
        r = requests.get(requestUrl)
        if r.status_code == 200:
            data = r.json()
            return data
        else:
            return None
    
    def sendKeyboard(self, chat_id, text, keyboard):
        requestUrl = self.TGurl + "sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": text,
            "reply_markup": json.dumps({"keyboard": keyboard, "resize_keyboard": True, "one_time_keyboard": True})
        }
        requests.post(requestUrl, data=payload)

    def getactivity(self):
        requestUrl = self.boredurl
        r = requests.get(requestUrl)
        if r.status_code == 200:
            data = r.json()
            return data
        else:
            return None
        