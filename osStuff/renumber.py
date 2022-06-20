import os


def renum(theDir):
    count=0
    for i in os.listdir(theDir):
        count+=1
        newName=theDir+f"{count}) "+i
        print(newName)
        os.rename(theDir+i,newName)

def delNum(theDir):
    for i in os.listdir(theDir):
        if ")" in i:
            j=i.split(") ")
            print(j[1])
            os.rename(theDir+i,theDir+j[1])

thedir="C:\\Users\\gians\\Desktop\\picFromInsta\\"
#renum(thedir)
renum(thedir)