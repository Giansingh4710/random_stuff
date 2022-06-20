def getWords(phone,lst):
    d={
        "a":2,
        "b":2,
        "c":2,
        "d":3,
        "e":3,
        "f":3,
        "g":4,
        "h":4,
        "i":4,
        "j":5,
        "k":5,
        "l":5,
        "m":6,
        "n":6,
        "o":6,
        "p":7,
        "q":7,
        "r":7,
        "s":7,
        "t":8,
        "u":8,
        "v":8,
        "w":9,
        "x":9,
        "y":9,
        "z":9,
    }
    ans=[]
    for word in lst:
        num=""
        for letter in word:
            num+=str(d[letter])
        print(num,phone,num in phone)
        if num in phone:
            ans.append(word)
    print(ans)


num="3662277"
lst=["foo","bar","baz","foobar","emo","cap","car","cat"]
getWords(num,lst) #=[""]