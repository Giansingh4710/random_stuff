from mutagen.mp3 import MP3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs





def getLinksNTitles():
    url="https://www.youtube.com/c/ShriSarblohBungaNangali/videos"
    br = webdriver.Chrome('C:\\Users\\gians\\Desktop\\stuff\\chromedriver.exe')#,options=options)
    br.get(url)
    html = br.find_element_by_tag_name('html')
    for i in range(100):
        html.send_keys(Keys.END) #scroll to end of page
    content=br.page_source.encode('utf-8').strip()
    soup=bs(content,"lxml")
    thumbnails=soup.findAll("div",id="overlays")
    timeStamps=[i.find("ytd-thumbnail-overlay-time-status-renderer") for i in thumbnails]
    leng=[i.find("span") for i in timeStamps]
    print(len(leng))

getLinksNTitles()

#audio = MP3("example.mp3")
#print(audio.info.length)