import requests

RootLink="https://api.gurbaninow.com/v2/banis/"
def getBanis():
    file=open('./banis.json','w')
    file.write('{\n    "banis":[\n')
    for i in range(1,30):
        baniLink=RootLink+str(i)
        theData=baniInfo(baniLink)
        file.write("        "+str(theData)+',\n')
    file.write("        ]")
    file.write("}")
    file.close()

def baniInfo(link):
    data=requests.get(link).json()
    baniData={"bani_name":data['baniinfo']['unicode'],"bani":getLinesOfBani(data['bani'])}
    return baniData

def getLinesOfBani(lst):
    ans=""
    for i in lst:
        ans+=i['line']['gurmukhi']['unicode'] + '\n'
        ans+=i['line']['translation']['english']['default'] + '\n\n'
    return ans
    
getBanis()
