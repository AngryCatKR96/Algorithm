import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    finalString = list(sys.stdin.readline().strip())

    while finalString[0] != finalString[-1]:
        del finalString[0]
        del finalString[-1]
        if len(finalString) == 0:
            break
    
    if(len(finalString)==0):
        print(0)
    else:    
        print(len(finalString))
        
    
    