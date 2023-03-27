import sys
import random

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    breakPoint = 0
    
    #n = 200000
    #s = ""
    #for _ in range(n):
    #    s = s + chr(random.randrange(97,123))
    
    countList = [0]*26
    sumList = []
    for i in range(n):
        l = s[i]
        if countList[ord(l)-97] != 0 :
            breakPoint = i
            left = set(s[:i])
            right = set(s[i:])
            sumList.append(len(left)+ len(right))
        else:
            countList[ord(l)-97] = countList[ord(l)-97] + 1

    print(max(sumList))