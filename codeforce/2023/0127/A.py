import sys

PI = "314159265358979323846264338327"

t = int(sys.stdin.readline().strip())

resultList = [0]*t
for i in range(t):
    
    input = sys.stdin.readline().strip()
    
    count = 0
    for j in range(len(input)):
        if input[j] == PI[j]:
            count+=1
        else:
            break
    
    resultList[i] = count
    
for i in resultList:
    print(i)