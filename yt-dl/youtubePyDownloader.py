'''
YouTube Video Downloader
Author: Ayushi Rawat
'''

#import the package
from pytube import YouTube

def download(url):
    yt = YouTube(url)
    yt.streams.get_audio_only().download()
    yt.streams.get_highest_resolution().download()
    # vids=yt.streams.all();
    # for i in range(len(vids)):
        # print(f'{i}) {vids[i]}');
    # ind=int(input("Which Video do you want to download: "))
    # vids[ind].download();
url = 'https://youtu.be/lc1Q65V3YdI'
download(url);


