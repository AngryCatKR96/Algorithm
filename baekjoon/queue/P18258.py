import sys
from collections import deque

N = int(input())

queue = deque()
for _ in range(N):
    comd = sys.stdin.readline().strip()
    
    if comd == "pop":
        try:
            print(queue.popleft())
        except:
            print(-1)
    elif comd == "size":
        print(len(queue))
    elif comd == "empty":
        if len(queue) == 0:
            print(1)
        else: 
            print(0)
    elif comd == "front":
        try:
            print(queue[0])
        except:
            print(-1)
    elif comd == "back":
        try:
            print(queue[-1])
        except:
            print(-1)
    else:
        P, X = comd.split()
        queue.append(int(X))
        
            