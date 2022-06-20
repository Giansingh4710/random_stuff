import pyautogui
import webbrowser
import datetime,time

def goToClass(timee,date,link):
    if ":" in timee[0:2]:
        timee="0"+timee
    classTime=timee.upper()+" "+date #timee format- 00:00 pm/am   date format- Apr 17  (the abriviation and date)
    a=datetime.datetime.now()
    nowTime=a.strftime("%I:%M %p %b %d") #11:02 AM Apr 17
    nowTime=nowTime.upper()
    classTime=classTime.upper()
    if classTime==nowTime or getMins(nowTime)>getMins(classTime):
        webbrowser.open(link)
        time.sleep(3)
        startClass(link)
        return True
    else:
        return False

def getMins(timeStr):
    monDict={"jan":31,"feb":28,"mar":31,"apr":30,"may":31,"jun":30,"jul":31,"aug":31,"sep":30,"oct":31,"nov":30,"dec":31}
    months=["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]

    pmDict={12:12,1:13,2:14,3:15,4:16,5:17,6:18,7:19,8:20,9:21,10:22,11:23}
    amDict={12:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:11}
    month=timeStr[9:12].lower()
    monthInd=months.index(month)

    days=int(timeStr[13:15])
    for i in range(monthInd):
        days+=monDict[months[i]]

    hoursInMins=int(timeStr[:2])
    if "am" in timeStr.lower():
        hoursInMins=amDict[hoursInMins]*60  #hours passed in mins
    elif "pm" in timeStr.lower():
        hoursInMins=pmDict[hoursInMins]*60  #hours passed in mins
    minutes=int(timeStr[3:5])
    daysInMin=days*24*60
    total=minutes+hoursInMins+daysInMin
    return total

def startClass(link):
    if "webex" in link.lower():
        button1=[]
        button2=[]
        for green in range(2):  # range 2 because sometimes you have to click the green button two times
            time.sleep(2)
            im=pyautogui.screenshot()
            #im.save("im.png")
            for i in range(10,1920):    
                for j in range(10,1080):   #these two loops go through every pixel.
                    px = im.getpixel((i, j))  #if the pixel matches the rgb of the the start button, it will click it
                    if px==(0,130,59):
                        if green==0:
                            button1.append((i,j))
                        else:
                            if (i,j) not in button1:
                                button2.append((i,j))
            if green==0:
                pyautogui.moveTo(button1[0])
                pyautogui.click()
            else:
                try:
                    pyautogui.moveTo(button2[0])
                    pyautogui.click()
                except IndexError:
                    print("No need for 2 clicks")
    elif "zoom" in link.lower():
        pyautogui.moveTo(1080,280)
        pyautogui.click()
        time.sleep(5)
        pyautogui.moveTo(1250,800)
        pyautogui.click()

def getClass(name="no"):
    AMCTutor="https://njit.webex.com/njit/j.php?MTID=mc1d5c2c4c1a9e6289a182b8cd25b94f2"
    vidyaGranths="https://washington.zoom.us/j/99487089871"
    BhaiNandLalJi="https://yorku.zoom.us/j/97735550671"
    times={"AMCTutor":["12:01 am"],"vidyaGranths":["09:15 pm"],"BhaiNandLalJi":["09:30 am"]}
    classLinks={"vidyaGranths":vidyaGranths,"AMCTutor":AMCTutor,"BhaiNandLalJi":BhaiNandLalJi}
    lst=["AMCTutor","vidyaGranths","BhaiNandLalJi"]
    if name not in lst:
        for i in range(len(lst)):
            print(f"{i+1}) {lst[i]}")
        name=lst[int(input("Select class do you want to join?: "))-1]
        possibleTimes=times[name]
    else:
        possibleTimes=times[name]
    if len(possibleTimes)==1:
        theTime=times[name][0]
    else:
        for i in range(len(possibleTimes)):
            print(f"{i+1}) {possibleTimes[i]}")
        theTime=int(input("Select the the Time: "))-1
        theTime=possibleTimes[theTime]
    link=classLinks[name]
    return link,theTime



#link,clTime=getClass()
#date="Apr 23"
#link="https://njit.webex.com/meet/gs4"
#print(goToClass(clTime,date,link))
#goToClass(clTime,date,link)


#run this loop and the you can leave or sleep etc and you will be loged into class.

link,theTime=getClass()
todayDate=datetime.datetime.now().strftime("%b %d") #Apr 17

counter=0
while True:
    counter+=1
    if goToClass(theTime,todayDate,link):
        print(f"It took {counter} tries")
        a=datetime.datetime.now()
        nowTime=a.strftime("%I:%M %p %b %d")
        print(nowTime)
        break
    else:
        print("Sleeping...")
        time.sleep(120.0)