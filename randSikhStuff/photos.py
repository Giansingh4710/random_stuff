from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import time
options = webdriver.ChromeOptions()
options.headless = True


def photos(urll):
    br = webdriver.Chrome('C:\\Users\\gians\\Desktop\\stuff\\chromedriver.exe')#,options=options)
    br.get(urll)
    time.sleep(5)
    #html = br.find_element_by_tag_name('html')
    content=br.page_source.encode('utf-8').strip()
    soup=bs(content,"lxml")
    cont=soup.find("div",class_="xfzUCb WQusHb")
    pictres=cont.findAll("div",class_="rtIMgb fCPuz")
    for i in pictres:
        atag=i.find("a")
        print("https://photos.google.com"+atag["href"])
    print(len(pictres))

url="https://photos.google.com/share/AF1QipMyPviVP7DMbs7BAu0s1vQd98mDdm5VwhSPRXIH6jIN2UvRx16lp5GnfuQ3OpCNqg?key=RUVYVlY3RTRnbE5SN1JNLW5zdHJNZGEyTTVQNnB3"
photos(url)
