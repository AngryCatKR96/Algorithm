import sys

def room(k,n):
    if k==0:
        return n
    elif n==1:
        return 1
    else:
        return room(k,n-1)+room(k-1,n)
    
T = int(sys.stdin.readline())

list = []

for _ in range(0,T):
    K = int(sys.stdin.readline())
    N = int(sys.stdin.readline())
    list.append(room(K,N))
    
for i in list:
    print(i)
    