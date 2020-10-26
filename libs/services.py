# cRadio 2020
import hashlib
import random
import threading

myr_domains = ["ru", "kz", "ua", "by"]

def calculateToken(winGuid):
    # It took an hour to detect which encoding is used
    return hashlib.md5(winGuid.encode('utf-16le')).hexdigest()

def getFakeToken():
    randData = ""
    for _ in range(random.randint(8, 24)):
        randData += chr(random.randint(97, 122))
    return calculateToken(randData)

def fancyNumbers(num):
    # Was in original client for Human-like number representation
    if num > 1000000:
        return str(num // 1000000) + "M"
    if num > 10000:
        return str(num // 1000) + "K"
    return str(num)

def checkMYRMail(mail):
    return mail.split(".")[-1] in myr_domains
