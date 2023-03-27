import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    inputList = list(map(int,sys.stdin.readline().strip().split()))
    
    for i in range(n):
        if i == n-1:
                break
        if inputList[i] >= 0:
            continue
        else:
            if inputList[i+1] <= 0:
                inputList[i] = -(inputList[i])
                inputList[i+1] = -(inputList[i+1])
            else:
                if abs(inputList[i]) > abs(inputList[i+1]):
                    inputList[i] = -(inputList[i])
                    inputList[i+1] = -(inputList[i+1])
                    
    print(sum(inputList))
                