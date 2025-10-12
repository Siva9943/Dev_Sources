def reversedFun(s):
    word=s.split(".")
    words=""
    for i in range(len(word)-1,-1,-1):
        words+=word[i]
        if i!=0:
            words+="."
    return words
print(reversedFun("..the..word.is.siva"))
