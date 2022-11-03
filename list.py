import requests
import os,runpy
#print("current working directory",os.getcwd())
#print("web scrap")
#r=requests.get('https://www.setopati.com')
#print(r.status_code)

def scrap():
    print("web scrap")
    r=requests.get('https://www.setopati.com')
    print(r.status_code)
   # print("current working directory",os.getcwd())

scrap()