import sys

def fibo(N):
    if N==0:
        return 0
    elif N==1:
        return 1
    else:
        return fibo(N-1)+fibo(N-2)
    
N = int(sys.stdin.readline().strip())

print(fibo(N))