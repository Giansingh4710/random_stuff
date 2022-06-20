import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.headless = True

url="https://gurbaninow.com/page/149?source=1"
br =  webdriver.Chrome('C:\\Users\\gians\\Desktop\\stuff\\chromedriver.exe',options=options)
br.get(url)

time.sleep(2)

content=br.page_source.encode('utf-8').strip()
#content=requests.get(url).text
soup=bs(content,"lxml")
conta=soup.find("div",id="shabad")
gurmukhi=conta.findAll("div",class_="gurmukhi unicode normal")
pangtia=[i.text.split() for i in gurmukhi]
wordsLst=[]
for pangti in pangtia:
    wordsLst+=pangti

maxx=0
for i in wordsLst:
    if len(i)>maxx:
        maxx=len(i)
print(maxx)
