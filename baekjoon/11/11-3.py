import sys

def recursion(s, l, r):
    global count
    count+=1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

T = int(sys.stdin.readline().strip())

resultList = [[0 for _ in range(2)] for _ in range(T)]
for i in range(T):
    count = 0
    stringInput = sys.stdin.readline().strip()
    resultList[i][0] = isPalindrome(stringInput)
    resultList[i][1] = count
    
for i in range(T):
    print(resultList[i][0], end=" ")
    print(resultList[i][1])
    
    
    
