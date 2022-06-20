import os
from mutagen.mp3 import MP3


totalTracks=0
def goThroughFiles(dir,timeInSeconds=0):
    for thing in os.listdir(dir):
        print(thing)
        if thing=="System Volume Information": continue
        path=dir+"\\"+thing
        if os.path.isdir(path):
            timeInSeconds+=goThroughFiles(path)
        elif os.path.isfile(path):
            try:
                audio=MP3(path)
                timeInSeconds+=audio.info.length
                global totalTracks
                totalTracks+=1
            except Exception:
                print("Could Not Convert")
                break
    return timeInSeconds                     


def nicePrint(seconds):
    print(f"There are a total of {seconds} seconds of audio which is also:")
    minutes=seconds/60
    print(f"Minutes: {minutes}")
    hours=minutes/60
    print(f"Hours: {hours}")
    days=hours/24
    print(f"Days: {days}")

    fullDays=seconds//(60*60*24)
    timeleft=seconds-fullDays*(60*60*24)
    fullHour=timeleft//(60*60)
    timeleft=timeleft-fullHour*(60*60)
    fullminutes=timeleft//60
    timeleft=timeleft-fullminutes*60
    print("So in total:", end=" ")
    print(f"{int(fullDays)} days, {int(fullHour)} hours, {int(fullminutes)} minutes, {int(timeleft)} seconds")


directory=input("Enter the path of the directory: ")
os.chdir(directory)

a=goThroughFiles(directory); 
nicePrint(a)
print(totalTracks)