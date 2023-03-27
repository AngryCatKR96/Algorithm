import sys

N, M = map(int,input().split())

basket = [0 for _ in range(N+1)]

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    for num in range(i,j+1):
        basket[num] = k
        
for num in range(1,N+1):
    print(basket[num], end=" ")