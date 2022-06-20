from bs4 import BeautifulSoup as bs
import requests

def getVidId(vid):
    #https://www.youtube.com/watch?v=vPMSshx7Czg
    lst=vid.split('?v=')
    return lst[-1]

def vidApiLink(id):
    apiKey="AIzaSyA-N-40HU1n9CYPW7wbZf6QQXMczHkaKlE"
    link=f'https://www.googleapis.com/youtube/v3/videos?id={id}&key='
    link+=apiKey
    link+='&fields=items(id,snippet(channelId,title,categoryId),statistics)&part=snippet,statistics'
    return link

def channelApiLink(id):
    apiKey="AIzaSyA-N-40HU1n9CYPW7wbZf6QQXMczHkaKlE"
    link=f'https://www.googleapis.com/youtube/v3/search?key={apiKey}&channelId={id}'
    link+='&part=snippet,id&order=date'
    return link

def getVidStat(link):
    res=requests.get(link)
    res=bs(res.text,'html.parser')
    print(res)


vid='https://www.youtube.com/watch?v=vPMSshx7Czg'
link=vidApiLink(getVidId(vid))
id="UC8B7EIN0EeqbZ2oQptkiQlA"
#link=vidApiLink(id)
#getVidStat(link)
print(channelApiLink(id))
