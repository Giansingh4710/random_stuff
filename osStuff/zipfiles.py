import zipfile
import os


path=r"C:\Users\gians\Downloads\takeout-20210506T173700Z-"

paths=[path+str(i+1).zfill(3)+".zip" for i in range(15)]

dir=r"C:\Users\gians\Desktop\DownloadedData\Google\Download2"


for i in range(15):
    with zipfile.ZipFile(paths[i+1], 'r') as zip_ref:
        try:
            zip_ref.extractall(dir)
            os.rename(r"C:\Users\gians\Desktop\DownloadedData\Google\Download2\Takeout",
            r"C:\Users\gians\Desktop\DownloadedData\Google\Download2\Takeout"+str(i+1))
        except Exception:
            print(i)
#zipp=zipfile.ZipFile(path,"r")
#zipp.extractall(dir)
