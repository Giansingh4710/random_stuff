import imaplib,email,re
import sendIfRight


class readEmail():
    def run(self):
        host="imap.gmail.com"
        user='shastarprice@gmail.com'
        password='etraibzhladpaupx'

        mail=imaplib.IMAP4_SSL(host)
        mail.login(user,password)
        mail.select("inbox")

        _, searchData=mail.search(None,"UNSEEN")
        for num in searchData[0].split():
            _, data=mail.fetch(num,"(RFC822)")
            _,b=data[0]
            emailMessage = email.message_from_bytes(b)
            whoSent = emailMessage["From"]

            theNumber = whoSent.split("@")[0]
            carrier=whoSent.split("@")[1]

            a = re.search("[0-9]{10}", theNumber)
            if a == None:
                continue
            for part in emailMessage.walk():
                if part.get_content_type() == "text/plain" or part.get_content_type() == "text/html":
                    body = part.get_payload(decode=True)
                    mms=self.getCarrier(carrier)

                    sentFromPhone = body.decode()
                    sentFromPhone = sentFromPhone.split(",")

                    phone = theNumber + mms
                    if len(sentFromPhone)!=2:
                        sendIfRight.sendmail("Not Valid","Please enter the ebay link and the price you want. exp: thelink, theprice",phone)
                        break

                    theLink=sentFromPhone[0].strip()
                    thePrice=sentFromPhone[1].strip()
                    thePrice=int(thePrice)
                    
                    sendIfRight.getPrice(theLink,thePrice,phone)

    def getCarrier(self,car):
        opts={'txt.att.net': '@mms.att.net', 'sms.myboostmobile.com': '@myboostmobile.com', 'mms.cricketwireless.net': '@mms.cricketwireless.net', 'msg.fi.google.com': '@msg.fi.google.com', 'messaging.sprintpcs.com': '@pm.sprint.com', 'vtext.com': '@vzwpix.com', 'tmomail.net': '@tmomail.net', 'message.ting.com': '@message.ting.com', 'email.uscc.net': '@mms.uscc.net', 'vmobl.com': '@vmpix.com', 'mms.att.net': '@mms.att.net', 'myboostmobile.com': '@myboostmobile.com', 'pm.sprint.com': '@pm.sprint.com', 'vzwpix.com': '@vzwpix.com', 'mms.uscc.net': '@mms.uscc.net', 'vmpix.com': '@vmpix.com'}
        return opts[car]

a=readEmail()
a.run()