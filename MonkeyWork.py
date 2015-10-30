import string, random
letters = list(set(string.ascii_letters.lower()+" "))

def randString(str):
    res = str
    letNum = 28 - len(str)
    for i in range(letNum):
        res+=random.choice(letters)
    return res

def checkString(str):
    base = "methinks it is like a weasel"
    count = 0
    for i in range(len(base)):
        if base[i] == str[i]:
            count+=1
        else:
            break            
    return (float(count)/len(base)*100, str[0:count])

def monkeyWork():
    bestString = ""
    bestScore = 0
    iter = 1
    while bestScore != 100:
        str = randString("")
        (res, temp) = checkString(str)
        if res > bestScore:
            bestScore = res
            bestString = str
        if iter % 1000 == 0:
            print("Best string: %s, best score %.2d, iter %d" %(bestString, bestScore, iter))
        iter+=1

def monkeyWork2():
    bestString = ""
    bestScore = 0
    curMatch = ""
    iter = 1
    while bestScore != 100:
        str = randString(curMatch)
        (res, temp) = checkString(str)
        if res > bestScore:
            bestScore = res
            bestString = str
            curMatch = temp
        if iter % 1000 == 0:
            print("Best string: %s, best score %.2d, iter %d" %(bestString, bestScore, iter))
        iter+=1

monkeyWork()
        
