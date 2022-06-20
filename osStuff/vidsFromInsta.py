import os
import shutil
main="C:\\Users\\gians\\Desktop\\giansingh4710_20210426\\"

counter=0
def getInsta(main):
    for thing in os.listdir(main):
        newMain=main+thing+"\\"
        if ".mp4" in thing or "jpg" in thing or ".png" in thing:
            #print(newMain)
            shutil.copy(newMain[:-1],f"C:/Users/gians/Desktop/picFromInsta")
        elif os.path.isdir(newMain):
            getInsta(newMain)
getInsta(main)
