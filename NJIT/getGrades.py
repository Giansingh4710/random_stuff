import sys
sys.path.append(r"C:\Users\gians\Desktop\CS\pythons\randomstuff")
import passwords 


import smtplib
from email.message import EmailMessage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

chrome_options = Options()
chrome_options.add_argument("--headless")
#chrome_options.add_argument={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}#my user agent

'''
from flask import Flask
from threading import Thread
app=Flask(' ')
@app.route('/')
def home():
  a="Daas is Alive!!"
  return a
def run():
  app.run(host="0.0.0.0", port=8080)
def KeepAlive():
  t=Thread(target=run)
  t.start()

KeepAlive()
'''

def signIn():
    url="https://portal.njit.edu/web/home-community/student-services"
    br = webdriver.Chrome('C:\\Users\\gians\\Desktop\\stuff\\chromedriver.exe')#,options=chrome_options)
    br.get(url)
    ucid=br.find_element_by_css_selector('#username')
    ucid.send_keys('Gs4')
    passw=br.find_element_by_css_selector("#password")


    passw.send_keys(passwords.NJITPASS)
    br.find_element_by_css_selector('body > div > div.the-content-row > div > div.col-md-8.left-col > form > div.cta-wrapper > button').click()
    br.find_element_by_css_selector('#accept').click()
    br.find_element_by_css_selector("#submitbtn").click()
    return br

def grades(br,semester="2021 Spring"):
    semesterTerm=br.find_element_by_css_selector("#term_id")
    opts=semesterTerm.find_elements_by_css_selector("option")
    for i in opts:
        if i.text==semester:
            i.click()
            break
    gradeTable=br.find_element_by_css_selector("#sga_portletDataTable > tbody")
    trTags=gradeTable.find_elements_by_tag_name("tr")
    for i in trTags:
        i.click()
    trTags=gradeTable.find_elements_by_tag_name("tr")
    final=[]
    for i in range(0,len(trTags),2):
        title=trTags[i].text
        finalGrade=trTags[i+1].text.split("\n")[-1]
        theGrade=(title,finalGrade)
        final.append(theGrade)
    br.quit()
    return final

def sendToPhone(subject,body,to):
    msg=EmailMessage()

    user='giansingh131313@gmail.com'
    password='jkodhyxiypnsdifl'

    msg["From"]=user
    msg['Subject']=subject
    msg["To"]=to
    msg.set_content(body)
    

    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg,mail_options='SMTPUTF8')
    server.quit()


classesAndGrades={} #grades when i start server
driver=signIn()
allGrades=grades(driver)
for i in allGrades:
    classesAndGrades[i[0]]=i[1]
while True:
    driver=signIn()
    allGrades=grades(driver)
    theMsg=""
    for i in allGrades:
        if classesAndGrades[i[0]]!=i[1]:  #if the grade changes it will append to theMsg string and if the string isn't empty it will send me a sms
            theMsg+=f"{classesAndGrades[i[0]]} {i[1]}"
            classesAndGrades[i[0]]=i[1]
    if theMsg!="":
        sendToPhone("Your Grades",theMsg,"6782670271@messaging.sprintpcs.com")
        print("Message Sent")
    else:
        print("No Change")
    sleep(3600)
    
    








    