

def decode(r):
    numInd=0
    letters="abcdefghijklmnopqrstuvwxyz"
    for i in range(len(r)):
        if r[i] not in "0123456789":
            numInd=i
            break
    numCode=r[:numInd]
    wordCode=r[numInd:]
    ans=""
    for i in wordCode:
        num=letters.index(i)
        for j in range(26):
            if j*int(numCode)%26==num:
                ans+=letters[j]
                break
    print(ans)
    return ans
decode("761328qockcouoqmoayqwmkkic")
