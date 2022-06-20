def initialLetterCount(wordList):
    ans={}
    for word in wordList:
        if word[0] not in ans:
            ans[word[0]]=1
        else:
            ans[word[0]]+=1
    return ans
horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetterCount(horton))

def initialLetters(wordList):
    ans={}
    for word in wordList:
        if word[0] not in ans:
            ans[word[0]]=[word]
        else:
            if word not in ans[word[0]]:
                ans[word[0]].append(word)
    return ans
print(initialLetters(horton))

def shareOneLetter(wordList):
    ans={}
    for word in wordList:
        if word not in ans:
            ans[word]=[]
            for word2 in wordList:
                for letter in word2:
                    if letter in word:
                        if word2 not in ans[word]:
                            ans[word].append(word2)
                            break
    return ans
print(shareOneLetter(horton))