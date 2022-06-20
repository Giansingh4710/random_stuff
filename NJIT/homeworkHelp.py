#cs 288. wikiapedia, scrape pages AA to ZZ
import urllib.request
from bs4 import BeautifulSoup
import requests
import re
url="https://en.wikipedia.org/wiki/"
abc="abcdefghijklmnopqrstuvwxyz"
allUrls=[]
for i in abc:
    oneLet=url+i
    for j in abc:
        twoLets=oneLet+j
        allUrls.append(twoLets)
dict={}
for i in allUrls:
    res=requests.get(i)
    soup=BeautifulSoup(res.text, 'html.parser')
    a=soup.find_all("html")
    b=a[0].text.split()
    text=re.findall(r"[a-zA-Z]+", str(b))
    for word in text:
        if word not in dict:
            dict[word]=1
        else:
            dict[word]+=1
    # break
allWords=[i for i in dict.keys()]
allNums=[i for i in dict.values()]

for i in range(15):
    maxx=max(allNums)
    ind=allNums.index(maxx)
    theWord=allWords[ind]
    print(maxx,end=" ")
    print(theWord)
    allNums.remove(maxx)
    allWords.remove(theWord)