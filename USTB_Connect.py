import time
import requests
import re

#######################################################

id = input("输入学号：")

psw = input("输入密码：")


#########################################################

class Login:

    def __init__(self):

        self.every = 30


    def login(self):


        print(self.getCurrentTime())

        url = "http://202.204.48.66/"

        headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Content-Length':'55',
        'Content-Type':'application/x-www-form-urlencoded',
        'Cookie':'__guid=60303022.1266821893518176300.1531809304239.62; myusername=%s; ' % id +
                 'username=%s; monitor_count=12' % id,
        'Host':"202.204.48.66",
        'Origin':"http://202.204.48.66/",
        'Referer':"http://202.204.48.66/",
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        }

        data = {
            'DDDDD': id,
            'upass': psw,
            'v6ip': '',
            '0MKKey': '123456789'
        }

        try:
            requests.post(url, headers=headers, data=data)
            print(self.getCurrentTime())
        except:
            print("error")



    def canConnect(self):
        try:
            q = requests.get("http://www.baidu.com", timeout=5)
            m = re.search(r'STATUS OK', q.text)
            if m:
                return True
            else:
                return False
        except:
            print('error')
            return False



    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))


    def main(self):
        print(self.getCurrentTime(), "连接开始")
        while True:
            self.login()
            while True:
                can_connect = self.canConnect()
                if not can_connect:
                    print(self.getCurrentTime())
                    self.login()
                else:
                    print(self.getCurrentTime())
                time.sleep(self.every)
            time.sleep(self.every)


login = Login()
login.main()
