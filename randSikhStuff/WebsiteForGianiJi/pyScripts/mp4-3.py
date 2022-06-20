
import os
from  selenium import webdriver
import time
#br = webdriver.Chrome('C:\\Users\\gians\\Desktop\\stuff\\chromedriver.exe')#,options=options)
khatas="C:\\Users\\gians\\Desktop\\CS\\pythons\\small-projects\\SikhStuff\\WebsiteForGianiJi\\audio"
os.chdir(khatas)
count=137
def getNames():
    print(os.getcwd())
    for khata in os.listdir()[-6:]:
        noMp4=khata[:-4]
        if "yt1s.com - " in noMp4:
            noMp4=noMp4[11:]
        newTitle=changeTitle(noMp4)
        try:
            os.rename(khata,newTitle)
        except:
            print("can't rename file")
def changeTitle(title):
    global count
    count+=1
    br.get("https://www.google.com/search?q=gurmukhi+to+english")
    punjabiTextBox=br.find_element_by_css_selector("#tw-source-text-ta")
    punjabiTextBox.clear()
    punjabiTextBox.send_keys(title)
    time.sleep(2)
    eng=br.find_element_by_css_selector("#tw-target-text > span").text
    new=str(count)+") "+eng+".mp3"
    return new

def fixNums(): #the counting for the files was messed up so used this func to fix that
    count=0
    for i in os.listdir():
        count+=1
        lst=i.split(" ")
        title=str(count)+") "+' '.join(lst[1:])
        os.rename(i,title)
        print("Before : Now")
        print(i[:4]+" : "+title[:4])
def removeGianiJiName(): #one time things
    count=0 #in the final script, I will count how many letter match with the original title from the txt file. Removing "gurwinder singh" will help get better results
    for i in os.listdir():
        if "gurwinder singh" in i.lower():
            count+=1
            new=i.lower().replace("gurwinder singh","").strip()
            os.rename(i,new)
    print(count)
def changeName(): #one time things
    #so basically when I download the youtube videos, the titles had not matras on the letters so google translate cant translate all of them. No I will manually chang ethem        
    nonEng=[i for i in os.listdir() if i.isascii()==False]
    for i in nonEng:
        num=i.split(" ")[0]
        print(i)
        newTitle=input("Enter the new title: ")
        newTitle=num+newTitle+".mp3"
        os.rename(i,newTitle)
        print(newTitle+"\n")
changeName()

