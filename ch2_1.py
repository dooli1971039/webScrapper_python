import requests
from bs4 import BeautifulSoup

URL="https://www.indeed.com/jobs?q=python&limit=50&radius=25"
indeed_result=requests.get(URL)

indeed_soup=BeautifulSoup(indeed_result.text,"html.parser")

pagination=indeed_soup.find("div", class_="pagination")

pages=pagination.find_all("a")
spans=[]
for page in pages:
    spans.append(page.find("span"))
    
spans=spans[:-1]

for i in spans:
    print(i)
