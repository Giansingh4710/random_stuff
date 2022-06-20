from bs4 import BeautifulSoup
import webbrowser, random
from selenium import webdriver
op = webdriver.ChromeOptions()
op.headless = True
from requests_html import HTMLSession

session = HTMLSession()

def getLinks():
    link="https://www.sikhitothemax.org/sundar-gutka"
    #br = webdriver.Chrome('C:\\Users\\gians\\Desktop\\stuff\\chromedriver.exe',options=op)
    #br.get(link)
    r = session.get(link)
    r.html.render()
    a=r.html.find(".sgCards")
    b=a[0].find("div")
    for i in b:
        print(i.text)
    '''
    content=br.page_source.encode('utf-8').strip()
    soup=BeautifulSoup(content,"lxml")
    allBaniaDiv=soup.find("div",class_="sgCards")
    allBania=allBaniaDiv.find_all("a")
    links=[]
    banis=[]
    for i in allBania:
        links.append("https://www.sikhitothemax.org"+i["href"])
        banis.append(i.text)
    return links,banis
    '''
getLinks()
'''   
links,banis=getLinks()

while True:
    ind=random.randint(0,len(links)-1)
    print("\n")
    read=input(f"Would you like to read {banis[ind]}? [y/n]: ")
    if "y" in read.lower():
        webbrowser.open(links[ind])
        break
'''
