import requests
import os

def solution():
    print("Welcome to IsItDown.py!")
    print("Please write a URL or URLs you want to check. (seperated by comma)")
    urls=input().split(",")
    url_list=[]
    for url in urls:
        url_list.append(url.strip()) #공백 제거


    for url in url_list:
        if "." not in url: #잘못된 url
            print(url,"is not a valid URL.")
            continue;

        if "http://" not in url:    #http추가
            url="http://"+url   

        url=url.lower() #모두 소문자로 변환
        
        try:
            if requests.get(url).status_code == requests.codes.ok:
                print(url,"is up!")    
        
        except:
            print(url,"is down!")
    
solution()
while True:
    str=input("Do you want to start over? y/n ")
    if str.lower().strip()=="y":
        os.system('cls')
        solution()
    elif str.lower().strip()=="n":
        print("k. bye!")
        break;
    else:
        print("That's not a valid answer")