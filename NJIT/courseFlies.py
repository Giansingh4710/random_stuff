import sys
import urllib.request
sys.path.append(r"C:\Users\gians\Desktop\CS\pythons\randomstuff")
import passwords 
from bs4 import BeautifulSoup as bs

import smtplib
from email.message import EmailMessage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
import urllib.request
chrome_options = Options()
# chrome_options.add_argument("--headless")

def signIn(url):
    br = webdriver.Chrome('C:\\Users\\gians\\Desktop\\stuff\\chromedriver.exe',options=chrome_options)
    br.get(url)
    ucid=br.find_element_by_css_selector('#username')
    ucid.send_keys('Gs4')
    passw=br.find_element_by_css_selector("#password")


    passw.send_keys(passwords.NJITPASS)
    br.find_element_by_css_selector('body > div > div.the-content-row > div > div.col-md-8.left-col > form > div.cta-wrapper > button').click()
    br.find_element_by_css_selector('#accept').click()
    br.find_element_by_css_selector("#submitbtn").click()
    return br

def pickCourse(br,dirr):
    courses=br.find_elements_by_class_name("course-list-table-row")
    for i in range(len(courses)):
        try:
            name=courses[i].find_element_by_tag_name("a").text
            print(f"{i+1}) {name}")
        except Exception:
            break
    theCourse=courses[int(input("Enter the number corresponding to the class you want to download the files for: "))-1]
    name=theCourse.find_element_by_tag_name("a").text
    linkToCourse=theCourse.find_element_by_tag_name("a").get_attribute('href')
    name=validFolderName(name)
    dirr+=name+"\\"
    os.mkdir(dirr)
    br.close()
    print(linkToCourse)
    return linkToCourse,dirr


def downloadFlies(link,dirr):
    #os.chdir(dirr)
    br=signIn(link)
    homepage=br.find_element_by_id("course_home_content")
    sections=homepage.find_elements_by_class_name("item-group-condensed")
    for i in sections[1:-1]: #the last section is just blank 
      title=i.find_element_by_class_name("ig-header-title").text
      title=validFolderName(title)
      newDir=dirr+title+"\\"
      os.mkdir(newDir)
      container=i.find_elements_by_tag_name("li")
      for j in container: #j is each file in the drop down menu
        j=j.find_element_by_class_name("item_name")
        atag=j.find_element_by_tag_name("a")
        href=atag.get_attribute("href")
        name=atag.text
     
        d=getFileLink(href)
        txtFile=open(newDir+name+".txt","w")
        txtFile.write("Assignment:\n")
        txtFile.write(d["assignment"][0])
        txtFile.write("\nSubmission:\n")
        txtFile.write(d["submission"][0])
        txtFile.close()




def getFileLink(href):
  try:
    br=signIn(href)
    content=br.find_element_by_id("content")
    contentText=content.text
    contentAtags=content.find_elements_by_tag_name("a")
    for i in contentAtags:
      i.click()
  except Exception:
    print("Homework Assignment Part")

  try:
    submission=br.find_element_by_css_selector("#sidebar_content > div > div.content")
    subText=submission.text
    subAtags=submission.find_elements_by_tag_name("a")
    for i in subAtags:
      i.click()
  except Exception:
    print("NO submissions")

  return {"assignment":[contentText],"submission":[subText]}



def validFolderName(title):
  noGOs=["\n","\\","/",":","*","?",'"',"<",">","|"]
  for i in noGOs:
    if i in title:
      title=title.replace(i,"!")
  return title


url="https://njit.instructure.com/courses"
directoryToDowl="C:\\Users\\gians\\Desktop\\NJIT\\classes\\"
"""
driver=signIn(url)
courseLink,dirr=pickCourse(driver,directoryToDowl)
downloadFlies(courseLink,dirr)"""

# downloadFlies("https://njit.instructure.com/courses/14487",directoryToDowl)

def downloadOldMath():
  theDir="C:\\Users\\gians\\Desktop\\Math112\\fall2021"

  import time
  theUrl="https://njit.instructure.com/courses/15906/files"
  theUrl="https://njit.instructure.com/courses/19802/files"
  br=signIn(theUrl)
  time.sleep(3)
  pdfs=br.find_elements_by_class_name("ef-item-row")
  content=br.page_source.encode('utf-8').strip()
  soup=bs(content,"lxml")
  pdfss=soup.findAll("div",class_="ef-item-row")
  allFiles=[]
  for pdfBar in pdfss:
    atags=pdfBar.findAll("a")
    # print(atags[1].text,atags[1]["href"])
    # print(atags[2].text,atags[2]["href"])
    try:
      fileTitleNLink=[atags[0].text,atags[0]["href"]]
      allFiles.append(fileTitleNLink)
      # urllib.request.urlretrieve(atags[0]["href"],theDir+atags[0].text)
    except Exception as e:
      print(e)
  for link in allFiles:
    try:
      br.get(link[1])
    except Exception as e:
      print(e,link)

downloadOldMath()
# urllib.request.urlretrieve("https://njit.instructure.com/files/2114158","C:\\Users\\gians\\Desktop\\Math112\\TETSSS.pdf")




    