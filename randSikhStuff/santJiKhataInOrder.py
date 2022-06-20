import requests
from bs4 import BeautifulSoup as bs
import re
#For khata of sant Giani Gurbachan Singh ji
def onlyLinks(url):
    res=requests.get(url)
    soup=bs(res.text, "lxml")
    khatas=soup.find_all("table",cellpadding=4)
    khatas=khatas[4:-2]
    folderWithLinks={}
    for file in khatas:
        try:
            title=file.find("font",size="2",color="0069c6").text
        except AttributeError:
            print("No Good. But we caught it!!")#It got the ALL the text from the drop down menu and those don't have a 'color=0069c6' attribute
            continue
        newUrl="http://www.gurmatveechar.com/"+file.find("a").get("href")
        if "mp3" in newUrl.lower():
            if title not in folderWithLinks:
                folderWithLinks[title]=[newUrl]
            else:
                folderWithLinks[title].append(newUrl)
        else:
            newFolderWithLinks=onlyLinks(newUrl)
            folderWithLinks.update(newFolderWithLinks) 
    return folderWithLinks

def santJiKhataInOrder():
    angs=re.compile(r"(Ang(-||\s)([0-9]{1,4})(\+[0-9]{1,4})?)")
    url="http://www.gurmatveechar.com/audio.php?q=f&f=%2FKatha%2F01_Puratan_Katha%2FSant_Gurbachan_Singh_%28Bhindran_wale%29%2FGuru_Granth_Sahib_Larivaar_Katha"
    a=onlyLinks(url)
    print(len(a))
    titles=list(a.keys())
    links=list(a.values())
    theAngs=[0]*1430
    for i in range(len(titles)):
        b=angs.search(titles[i])
        ang=b.group(3) #the third group gives the ang
        num=int(ang)-1
        theAngs[num]=links[i]
    default="http://sikhsoul.com/audio_files/mp3/Bani/Kirtan%20Sohila/Bhai%20Tarlochan%20Singh%20Ragi%20-%20Kirtan%20Sohaila.mp3"
    d={}
    for i in range(len(theAngs)):
        if theAngs[i]==0:
            down=default
            name=int(1+i)
            print(name)
        else:
            down=theAngs[i]
            name=int(1+i)
        d[name]=down
    return d

a=santJiKhataInOrder()
