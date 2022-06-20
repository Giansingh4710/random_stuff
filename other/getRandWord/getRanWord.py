from selenium import webdriver
import passGen

def getSite():
    a=passGen.password()

    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280,720")
    options.add_argument("--no-sandbox")
    options.add_argument={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}#my user agent

    br = webdriver.Chrome('C:\\Users\\gians\\Desktop\\stuff\\chromedriver.exe',options=options)
    br.get("https://www.google.com/")
    typee=br.find_element_by_css_selector("body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")
    typee.send_keys(a)
    typee.submit()
    search=br.find_element_by_css_selector('#rso')
    sites=search.find_elements_by_tag_name('a')
    for i in sites:
        try:
            i.click()
            w=br.find_element_by_tag_name("html")
            wor=w.text
            print("success!!!!!!")
            break
        except:
            print(i.text)
            print("fail :( ")
    words=wor.split()
    url=br.current_url
    br.close()
    return words,url
def getWord():
    words,url=getSite()
    abc="QAZXSWEDCVFRTGBNHYUJMKIOLPqazxswedcvfrtgbnhyujmkilop"
    for word in words:
        lenWord=len(word)
        for i in word:
            if i in abc:
                lenWord-=1            
        if lenWord==0:
            ans=word[:]
            d=[ans,url]
            return d
#print(getWord())


#br.get_screenshot_as_file("screenshot.png")



