import requests
def getRandomShabad():
    url="https://api.gurbaninow.com/v2/shabad/random"
    shabadJson=requests.get(url).json()
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
print(getRandomShabad()[1])
