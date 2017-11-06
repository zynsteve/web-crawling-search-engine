import json
import requests

class YDMHttp(object):
    apiurl = 'http://api.yundama.com/api.php'
    username = ''
    password = ''
    appid = ''
    appkey = ''

    def __init__(self, username, password, appid, appkey):
        self.username = username
        self.password = password
        self.appid = str(appid)
        self.appkey = appkey

    def balance(self):
        data = {'method': 'balance', 'username': self.username, 'password': self.password, 'appid': self.appid, 'appkey': self.appkey}
        response_data = requests.post(self.apiurl, data=data)
        ret_data = json.loads(response_data.text)
        if ret_data["ret"] == 0:
            print ("Get Remaining Points!", ret_data["balance"])
            return ret_data["balance"]
        else:
            return None

    def login(self):
        data = {'method': 'login', 'username': self.username, 'password': self.password, 'appid': self.appid, 'appkey': self.appkey}
        response_data = requests.post(self.apiurl, data=data)
        ret_data = json.loads(response_data.text)
        if ret_data["ret"] == 0:
            print ("Login Successful!", ret_data["uid"])
            return ret_data["uid"]
        else:
            return None

    def decode(self, filename, codetype, timeout):
        data = {'method': 'upload', 'username': self.username, 'password': self.password, 'appid': self.appid, 'appkey': self.appkey, 'codetype': str(codetype), 'timeout': str(timeout)}
        files = {'file': open(filename, 'rb')}
        response_data = requests.post(self.apiurl, files=files, data=data)
        ret_data = json.loads(response_data.text)
        if ret_data["ret"] == 0:
            print ("Recognize Successful!", ret_data["text"])
            return ret_data["text"]
        else:
            return None

if __name__ == "__main__":
    username = 'da_ge_da1'
    password = 'da_ge_da'
    appid = 3129
    appkey = '40d5ad41c047179fc797631e3b9c3025'
    filename = 'getimage.jpg'
    codetype = 1004
    timeout = 60
    if (username == 'username'):
        print ('Please Try Again!')
    else:
        yundama = YDMHttp(username, password, appid, appkey)

        uid = yundama.login();
        print ('uid: %s' % uid)

        balance = yundama.balance();
        print ('balance: %s' % balance)

        text = yundama.decode(filename, codetype, timeout);
