#cRadio 2020
import requests as rq
import json

stdResolveText=" Here are some tips to solve your problem\n\t1) Make sure you have the latest version from github\n\t2) Up to date? Open an issue\nKTHXBYE"
class API:
    apiBaseUrl="http://myrz.org/api/"
    headers={'User-Agent': 'Chrome'}
    validated=False
    plus=False

    def __init__(self,token):
        self.token=token

    def checkStatusCode(self,code):
        if code == 200:
            pass
        elif code == 404:
            print("API directory was not found on this server."+stdResolveText)
            exit()
        elif code == 403:
            print("API server responded with 403 (Access denied)."+stdResolveText)
            exit()
        else:
            print("IDK what's happened but we got an error: "+code)

    def validateKey(self):
        conn = rq.get(self.apiBaseUrl+"check.php?plus=1&key="+self.token,proxies=proxies,headers=self.headers)
        self.checkStatusCode() #only once
        tmp=json.loads(conn.text)
        if "Access" in tmp["message"]:
            self.validated=True
            print("Key: Valid")
            if "Access" in tmp["plus"]:
                self.plus=True
                print("Plus: Valid")
                return 2
            return 1
        else:
            print("Key: Invalid")
            return 0
