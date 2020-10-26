#cRadio 2020
import requests as rq
import json
import threading

stdResolveText=" Here are some tips to solve your problem\n\t1) Make sure you have the latest version from github\n\t2) Up to date? Open an issue\nKTHXBYE"
class API:
    apiBaseUrl="http://myrz.org/api/"
    headers={'User-Agent': 'Chrome'}
    validated=False
    plus=False
    tmpDB=[]

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
        conn = rq.get(self.apiBaseUrl+"check.php?plus=1&key="+self.token,headers=self.headers)
        self.checkStatusCode(conn.status_code) #only once
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

    def searchValidThread(self,db_part):
        conn = rq.post(self.apiBaseUrl+"part_search.php",data={"key":self.token,"type":"noinsert","lines":db_part},headers=self.headers)
        tmp=json.loads(conn.text)
        list=[]
        for entry in tmp:
            if entry["is_private"]:
                list.append(entry["line"])
        self.tmpDB.extend(list)


    def searchValid(self,db):
        bulk=len(db)
        threads=[]
        while bulk>0:
            db_part=" ".join(db[len(db)-bulk:len(db)-bulk+299])
            searchThread = threading.Thread(target=self.searchValidThread,args=(db_part,))
            threads.append(searchThread)
            bulk-=300
        while threading.active_count() > 1:
            print(f"\r[Running][Threads:{threading.active_count()-1} Ready:{len(self.tmpDB)}]",end="")
            for i in range(len(threads)):
                

