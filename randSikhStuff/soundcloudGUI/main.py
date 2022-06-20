from selenium import webdriver
import time,os
from bs4 import BeautifulSoup as bs
import urllib.request 

import tkinter as tk
from tkinter import Scrollbar, HORIZONTAL
from tkinter.ttk import Progressbar
from tkinter import BOTTOM, X, RIGHT, Y, NONE, TOP, END
from tkinter import simpledialog       
import time
import webbrowser



options = webdriver.ChromeOptions()

def getBrowser():
    options.headless = is_headless
    br =  webdriver.Chrome('C:\\Users\\gians\\Desktop\\stuff\\chromedriver_win32\\chromedriver.exe',options=options)
    return br

def linksToPlayLists(url): #gets all the links to the playlists in soundcloud
    br=getBrowser()
    br.get(url)
    #time.sleep(4)
    scroll=0
    end=False
    while not end:
        print("scrolling to get all playlist links")
        firstScroll=br.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        time.sleep(3)
        if firstScroll==scroll:
            end=True
        else:
            scroll=firstScroll
    content=br.page_source.encode('utf-8').strip()
    soup=bs(content,"lxml")
    allPlaylists=soup.find("div",class_="userMain__content")
    allPlaylists=allPlaylists.find_all("li",class_="soundList__item")
    playlistLinks=[]
    for playlist in allPlaylists:
        atag=playlist.find("a",class_="soundTitle__title sc-link-dark sc-link-secondary")
        theLinkWithTitle=(atag.text.strip(),"https://soundcloud.com"+atag["href"])
        playlistLinks.append(theLinkWithTitle)
    br.close()
    return playlistLinks

def linksInPlaylist(playlists): #gets all the individual katha links inside the playlists
    d={}
    for playlist in playlists:
        title=playlist[0]
        link=playlist[1]
        print(f"getting all tracks for {title}")
        try:
            links=getLinksForPlaylist(link) #list of tuples where index 0 is title of link and index 1 is link
            d[title]=links
        except Exception:
            print(f"Playlist not downloaded: {title}")
    return d

def getLinksForPlaylist(link): #gets links for katha in a playlist. This func is used for the func above
    br=getBrowser()
    br.get(link)
    scroll=0
    end=False
    while not end:
        firstScroll=br.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        time.sleep(1)
        if firstScroll==scroll:
            end=True
        else:
            scroll=firstScroll
    atags=br.find_elements_by_css_selector("div > div.trackItem__content.sc-truncate > a")
    links=[(i.text,i.get_attribute('href')) for i in atags]
    br.close()
    return links

def downloadLinksInPlaylist(directory,obj):
    for playlist in obj:
        print(f"downloading {playlist}")
        newPlace=f"{directory}{playlist}\\"
        os.mkdir(newPlace)
        for track in obj[playlist]:
            print(f"downloading {track}")
            try:
                downloadLink(newPlace,track)
                t.insert(END,f'downloaded - {track}\n')
            except Exception:
                print(f"No Download - {track}")
                t.insert(END,f'ERROR while downloading - {track}\n')
            root.update_idletasks()

def downloadLink(dir,track):
    br=getBrowser()
    theUrl="https://soundcloudtomp3.app"
    br.get(theUrl)
    # time.sleep(5)
    entry=br.find_element_by_css_selector("body > div.jumbotron > div > center > form > div > input")
    entry.send_keys(track[1]) #track[1] is the soundcloud url link of katha
    button=br.find_element_by_css_selector("#fd")
    button.click()

    atag=br.find_elements_by_xpath('//*[@id="dlMP3"]')
    theDownloadLink=atag[2].get_attribute("href")
    urllib.request.urlretrieve(theDownloadLink,f'{dir}{track[0]}.mp3')
    time.sleep(1)
    br.close()


def mainScript(url):
    if url[-1]=="/":
        url=url[:-1]
    t.delete(f"0.0",END)
    path=simpledialog.askstring("Type","Enter the path were you want to download the files (exp: 'C:\\Users\\gians\\Desktop\\CS\\pythons\\small-projects\\SikhStuff'):")
    if path[-1]!="\\":
        path+="\\"
    print(path)
    os.chdir(path)
    label["text"]="Calculating..."
    root.update_idletasks()

    if url[-4:]=="sets":
        print("downlowding all playlists for the artist")
        artistName=url.split("/")[-2]
        path+=artistName+"\\"
        os.mkdir(path)
        listOfPlaylists=linksToPlayLists(url) #returns list of tuples. ind 0 of tuple=name of playlist, ind1 of tuple=link to playlist 
    else:
        print("downlowding 1 playlist")
        nameOfPlaylist=url.split("/")[-1] #last part of url is playlist name
        listOfPlaylists=[(nameOfPlaylist,url)]
    obj=linksInPlaylist(listOfPlaylists) #returns dict where key is playlist name and value is list of tuples of tracks in list. ind 0 of tuple=name of track, ind1 of tuple=link to track 
    downloadLinksInPlaylist(path,obj)
        

# url="https://soundcloud.com/vaheguru1313/sets/nitnem"
# mainScript(url)



#-------TKinter----------------

def openSoundcloud():
    webbrowser.open("https://soundcloud.com/")

def changeHeadlessOpt():
    global is_headless
    print(is_headless)

    if is_headless==False:
        headlessOpt.config(text="Computation will now be Hidden and done in the background (unstable. There might be bugs with the downloading of all the files")
        is_headless=True
    else:
        headlessOpt.config(text="Computation will now be Seen (more stable, but can get crazy (don't close any of the pop up windows))")
        is_headless=False


is_headless=False

root=tk.Tk()
root.title("Download any playlist from soundcloud")
root.geometry("1500x700")

instruction=tk.Label(root,fg="blue",bg="#80c1ff",font=("courier",11),text="Enter the link (in the yellow box) of the folder you want to download from Soundcloud:\nTo download 1 playlist, enter the playlist link. EXPAMPLE: 'https://soundcloud.com/bhaisukhasinghuk/sets/sikha-di-bhagatmala',\nTo download all the playlists from an artist, enter the link of the artist. EXPAMPLE: 'https://soundcloud.com/bhaisukhasinghuk/sets'.\n HINT: The link you put should have the word 'sets' in it")
instruction.pack(side="top",pady=10)

entry=tk.Entry(root,bg="yellow",width=150)
entry.pack()
forGui=[]

goToGV=tk.Button(root,font=("courier",8),text="click here to go to Soundcloud.com",bg="gray",
command=openSoundcloud
)
goToGV.pack()

button=tk.Button(root,font=("courier",12),text="click here after you have copy and pasted the link you want",bg="gray",
command=lambda: mainScript(entry.get())
)
button.pack()

headlessOpt=tk.Button(root,font=("courier",12),text="Computation will be Seen (more stable, but can get crazy (don't close any of the pop up windows))",bg="gray",
command=changeHeadlessOpt
)
headlessOpt.pack()


label=tk.Label(root,width=45,height=4,bg="#80c1ff",font=("courier",13),text="It might take some time to download the files")
label.pack()

h = Scrollbar(root, orient = 'horizontal')
h.pack(side = BOTTOM, fill = X)

progress = Progressbar(root, orient = HORIZONTAL,length = 100, mode = 'determinate',)
progress.pack(pady = 10)

v = Scrollbar(root)
v.pack(side = RIGHT, fill = Y)
t = tk.Text(root, wrap = NONE,xscrollcommand = h.set,yscrollcommand = v.set)
t.pack(side=TOP,fill="both")
h.config(command=t.xview)
v.config(command=t.yview)


root.mainloop()