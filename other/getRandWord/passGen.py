import random,pyperclip

#all="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm,<.>/?'[]}{!@#$%^&*()_=1234567890-=/*-+`~"
all="1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
def password():
    passworrd=""
    size=3
    allorsome="yes"
    for i in range(size):
        ind=random.randrange(0,len(all));
        passworrd+=all[ind]        
    return passworrd
#print(password())





