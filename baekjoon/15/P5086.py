import sys

while(True):
    N, M = map(int,sys.stdin.readline().strip().split())
    if N==0 and M==0:
        break
    
    if N<M and M%N == 0:
        print("factor")
    elif N>M and N%M == 0:
        print("multiple")
    else:
        print("neither")
        
