import urllib.request
from bs4 import BeautifulSoup as bs 
import requests
import time


StupidLongVariablecounterBecauseItIsGlobal=0
def GurmatVeecharLink(url):	
    res=requests.get(url)
    soup=bs(res.text, 'lxml')
    khatas=soup.find_all("table",cellpadding=4)
    khatas=khatas[4:-2]
    return getAllLinks(khatas)

def getAllLinks(khatas):
    linksWithTitles={}
    for file in khatas:
        newUrl="http://www.gurmatveechar.com/"+file.find("a").get("href")
        if "mp3" in newUrl.lower():
            global StupidLongVariablecounterBecauseItIsGlobal
            StupidLongVariablecounterBecauseItIsGlobal+=1
            title=f"{str(StupidLongVariablecounterBecauseItIsGlobal)} ) {file.text}"
            linksWithTitles[title]=newUrl
        else:
            newLinkWithTitles=GurmatVeecharLink(newUrl)
            linksWithTitles.update(newLinkWithTitles)
    return linksWithTitles
def getSize():
    import re
    mb=re.compile(r"([0-9]{1,3}(\.[0-9]*)?\s(MB)|(KB))")
    allMbs=""
    MBsum=0
    for i in khatas:
        allMbs+=i
    for i in mb.findall(allMbs):
        try:
            val=float(i[0][:-3])
            if val>10:
                print(val)
        except:
            print("failed to convert to float")
        MBsum+=val

    '''for i in khatas:
        title=i[:-40]+".mp3"
        finalUrl=khatas[i]
        #urllib.request.urlretrieve(finalUrl,f"D:\\SwamiRamSinghJi\\{title}")
        print(f'{title} - {finalUrl}')
    '''

    print(MBsum)
khatas=GurmatVeecharLink("http://www.gurmatveechar.com/audio.php?q=f&f=%2FKatha%2F02_Present_Day_Katha%2FSwami_Ram_Singh_Nirmala")
getSize()