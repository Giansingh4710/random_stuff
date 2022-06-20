#1
def hasFinalLetter(strList,letters):
    answer=[]
    for word in strList:
        for letter in letters:
            if word[-1]==letter:
                answer.append(word)
    print(answer)
    return answer

lst=["yo","you","from","punjab"]
letters=["o","a"]
hasFinalLetter(lst,letters)

lst=["I","am","als0","from","there"]
letters=["m","e"]
hasFinalLetter(lst,letters)

lst=["hello","bobby","john"]
letters=["o","n"]
hasFinalLetter(lst,letters)

#2
def isDivisible(maxInt,twoInts):
    answer=[]
    for i in range(maxInt):
        if i%twoInts[0]==0 and i%twoInts[1]==0:
            answer.append(i)
    print(answer)
    return answer

isDivisible(1,(10,50))
isDivisible(1,(10,50))
isDivisible(1,(10,50))

