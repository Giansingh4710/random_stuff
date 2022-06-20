from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import time
from datetime import datetime as dt

options = webdriver.ChromeOptions()
options.headless = True

url="https://www.youtube.com/c/ShriSarblohBungaNangali/videos"

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
    videosViews=[]
    d={}
    print(len(vids))
    hrefs=["https://www.youtube.com"+i.get("href") for i in vids] #hrefs from the videos
    for i in range(0,len(span),2):
        viewsNhowLongAgo=[] # a list of size 2 where index 0 in the views and index 1 is how long ago
        viewsNhowLongAgo.append(span[i].text) #span[i].text is views
        viewsNhowLongAgo.append(span[i+1].text) #THIS IS how long ago video made like ' 2 months ago'
        videosViews.append(viewsNhowLongAgo)
    for i in range(len(vids)):
        title=vids[i].text
        d[title]=videosViews[i]
        d[title].append(hrefs[i])
    br.close()
    return d

def writeInFile(dictt):
    br = webdriver.Chrome('C:\\Users\\gians\\Desktop\\stuff\\chromedriver.exe')#,options=options)
    br.get("https://www.google.com/search?q=gurmukhi+to+english")
    punjabiTextBox=br.find_element_by_css_selector("#tw-source-text-ta")
    filee=open("C:\\Users\\gians\\Desktop\\WebsiteForGianiJi\\GianGurwinderSinghJi.txt","w")
    count=0
    for i in dictt:
        count+=1
        link=dictt[i][-1]
        print(link)
        try:
            filee.write(str(count)+") "+i+" $$$ "+" # ".join(dictt[i])+"\n")
        except UnicodeEncodeError:
            #print(i+" : Going to google and translating the Gurmukhi title")
            punjabiTextBox.clear()
            punjabiTextBox.send_keys(i)
            time.sleep(1)
            eng=br.find_element_by_css_selector("#tw-target-text > span").text
            try:
                filee.write(str(count)+") "+eng+" $$$ "+" # ".join(dictt[i])+"\n")
            except UnicodeEncodeError:
                filee.write(f"GianiGurwinderSingh Ji Video {count}"+" $$$ "+" # ".join(dictt[i])+"\n")
    time.sleep(5)
    filee.close()

def getLinks(): #I already wro the program to get the links and write to a text file. So instead of geting it from youtube everytime, I will just read the text file as it is faster.
    filee=open("C:\\Users\\gians\\Desktop\\WebsiteForGianiJi\\GianGurwinderSinghJi.txt","r")
    data=filee.readlines()
    allKhatas=[]
    for i in range(len(data)):
        line=data[i];
        dictform=line.split(" $$$ ");
        lst=dictform[1].split(" # ");
        link=lst[2];
        allKhatas.append(link[:-1]) # remove new line \n
    return allKhatas
def downloadLinks(links): 
    br = webdriver.Chrome('C:\\Users\\gians\\Desktop\\stuff\\chromedriver.exe')#,options=options)
    for link in links:
        br.get(link)      
        time.sleep(2)
        for i in range(10):
            if i>5:
                time.sleep(10)
            try:                                         #https://www.youtube.com/watch?v=zKTHiS2UfVk
                br.find_element_by_id("btn-action").click()
                time.sleep(5)
                br.find_element_by_css_selector("#asuccess").click()
                time.sleep(5)
                break
            except:
                print("Error")

start=str(dt.now())

a=getLinksNTitles(url)
filee=open("InGurmukhi.txt",'w',encoding= "utf-8")
for i in a:
    print(i)
    filee.write(i+"\n")
filee.close()

end=str(dt.now())
print(f"Start: {start}")
print(f"End: {end}",end="\n\n")
startSeconds=(int(start[11:13])*60*60)+(int(start[14:16])*60)+int(start[17:19])
endSeconds=(int(end[11:13])*60*60)+(int(end[14:16])*60)+int(end[17:19])
print(f"Seconds: {endSeconds-startSeconds}")
print(f"Minutes: {(endSeconds-startSeconds)/60}")
print(f"Hours: {(endSeconds-startSeconds)/(60*60)}")

    



