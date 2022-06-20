'''
I while ago I downloaded an asa di vaar track from KeertanVibes youtube channel but the downloaded file got
corrupted so I went to youtube to find the track again and I can't find it. The title had MVI in it and was 
20 mins long
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import time
from datetime import datetime as dt

options = webdriver.ChromeOptions()
options.headless = True


def getLinksNTitles(urll):
    br = webdriver.Chrome('C:\\Users\\gians\\Desktop\\stuff\\chromedriver.exe')#,options=options)
    br.get(urll)
    html = br.find_element_by_tag_name('html')
    for i in range(100):
        html.send_keys(Keys.END) #scroll to end of page
    content=br.page_source.encode('utf-8').strip()
    soup=bs(content,"lxml")
    vids=soup.findAll("a",id="video-title") #this highlghts ALL the titles under the thumnail and has the href in it
    span=soup.findAll("span",class_="style-scope ytd-grid-video-renderer") # This gets the views and date(how long ago)
    videoLen=soup.findAll("span",class_="style-scope ytd-thumbnail-overlay-time-status-renderer")
    print(len(videoLen))
    print(len(vids))
    videosViews=[]
    d={}
    hrefs=["https://www.youtube.com"+i.get("href") for i in vids] #hrefs from the videos
    for i in range(0,len(span),2):
        viewsNhowLongAgo=[] # a list of size 2 where index 0 in the views and index 1 is how long ago
        viewsNhowLongAgo.append(span[i].text) #span[i].text is views
        viewsNhowLongAgo.append(span[i+1].text) #THIS IS how long ago video made like ' 2 months ago'
        videosViews.append(viewsNhowLongAgo)
    for i in range(len(vids)):
        title=vids[i].text
        lenOfVid=videoLen[i].text.strip()
        d[title]=[lenOfVid]
        d[title].append(hrefs[i])
    br.close()
    print(len(d))
    return d

url="https://www.youtube.com/c/KeertanVibes10k/videos"
theDict=getLinksNTitles(url)
for i in theDict:
    time=int(theDict[i][0].split(":")[0]) #theDict[i][0]== a time stamp like 32:32 so we split it by ":" and take the 0 index in that list and make it int
    if "MVI" in i and time>15:
        print(f"{i} : {theDict[i]}")

"""
and Jackpot this code will print out the track I was looking for. 
20 min asa di vaar. Gurparsadde. Maharj kirpa ji.
"""