import os
import time
count=0
def inOrder(dir):
    os.chdir(dir)
    print(os.getcwd())
    for file in os.listdir():
        if file!="System Volume Information":
            if os.path.isdir(file):
                inOrder(file)
                os.chdir("..")
            else:    
                global count
                count+=1
                lst=file.split(")")
                #title=str(count).zfill(3)+")"+"".join(lst[1:])
                title=str(count).zfill(3)+")"+"GianiSherSinghJiFacebook.mp3"
                print(title)
                #os.rename(file,title)

theDir="D:\\gianishersinghji"
inOrder(theDir)