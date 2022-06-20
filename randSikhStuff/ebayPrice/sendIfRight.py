import requests, smtplib
from bs4 import BeautifulSoup as bs
from email.message import EmailMessage
import smtplib
from threading import Thread

class SendIfRight(Thread):
    def run(self,url,priceToPay,who):
        res=requests.get(url)
        soup=bs(res.text,'lxml')
        price=soup.find(class_='mainPrice').text.strip()
        print(price)
        intprice=int(price[4:7])
        print(intprice)
        if intprice>priceToPay:
            body=f"The price is now {str(intprice)}.\nLink:{url}"
            self.sendmail("Ebay Price",body,who)
            print("Mail Sent")
        else:
            print('Price too high. No email send')
    def sendmail(self,subject,body,to):
        msg=EmailMessage()

        user='shastarprice@gmail.com'
        password='etraibzhladpaupx'

        msg["From"]=user
        msg['Subject']=subject
        msg["To"]=to
        msg.set_content(body)
        

        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(user,password)
        server.send_message(msg,mail_options='SMTPUTF8')
        server.quit()
a=SendIfRight()
a.run("https://www.ebay.com/itm/402689827308",111,"giansingh4710@gmail.com")




