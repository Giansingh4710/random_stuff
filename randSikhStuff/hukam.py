from bs4 import BeautifulSoup as bs
import requests

url="https://www.sikhnet.com/hukam";

res=requests.get(url);
soup=bs(res.text,'lxml')

hukam=soup.find('div',id="hukam-content")
test=soup.find('div', class_='t-gurmukhi colorblack')
for i in hukam: print(i.text)




