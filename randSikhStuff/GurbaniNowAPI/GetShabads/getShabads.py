import json
import requests
from requests.structures import CaseInsensitiveDict

# url = "https://api.gurbaninow.com/v2/hukamnama/today"

headers = CaseInsensitiveDict()
# headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0"
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
headers["Accept-Language"] = "en-US,en;q=0.5"
headers["DNT"] = "1"
headers["Connection"] = "keep-alive"
headers["Upgrade-Insecure-Requests"] = "1"

url='https://api.gurbaninow.com/v2/shabad/random'

def getRandomShabad():
    url="https://api.gurbaninow.com/v2/shabad/random"
    shabadJson=requests.get(url,headers=headers).json()
    shabadId=shabadJson['shabadinfo']['shabadid']
    angNum=shabadJson['shabadinfo']['pageno']
    shabadPangtiList=shabadJson['shabad']
    shabad=getShabadFromJson(shabadPangtiList,angNum)
    return [ shabadId,shabad ]

def getShabadFromJson(pangtiList,angNum):
    shabad=""
    for i in pangtiList:
        line=i['line']['gurmukhi']['unicode']
        translation=i['line']['translation']['english']['default']
        shabad+=line+"\n"+translation+"\n\n"
    return shabad

allShabads={}
shabadsFile=open('2NoRepeatsAllShabads.json','w',encoding='UTF-8')
for i in range(6000):
    a=getRandomShabad()
    id=a[0]
    shabad=a[1].replace("\"","\'").replace("\n","\\n")
    if id not in allShabads:
        allShabads[id]=shabad
        shabadsFile.write(f'"{id}" : "{shabad}",\n')
    else:
        print(f"Shabad alread read!")

shabadsFile.close()
print("--------------------")
print(allShabads)
# print(getRandomShabad())
