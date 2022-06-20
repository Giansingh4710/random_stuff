import os,random
#os.chdir("C:\\Users\\gians\\Desktop\\AkhandPathDelih2020")
#os.chdir("D:\\")
#print(os.getcwd())
#print(os.listdir())
num=random.randint(0,10)
#os.system("the file name")
    
count=0
def getName(dir):
    files=[]
    for i in os.listdir(dir):
        path=dir+i+"\\"
        if ".mp3" in i:
            files.append(path)
            global count
            count+=1
            
        else:
            if os.path.isdir(path):
                filesInFolder=getName(path)
                files+=filesInFolder
    return files
mainDir="D:\\"
files=getName(mainDir)
os.chdir(mainDir)
num=random.randint(0,len(files)-1)
print(files[num])
os.system(files[num][:-1])
 
#os.system("C:\\Users\\gians\\Desktop\\AkhandPathDelih2020\\Part1.mp3")