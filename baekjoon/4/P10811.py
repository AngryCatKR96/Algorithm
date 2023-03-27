import sys

N, M = map(int, input().split())

basket = []
for i in range(N+1):
    basket.append(i)
    
for _ in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())
    
    while i <= j:
        basket[i], basket[j] = basket[j], basket[i]
        i+=1
        j-=1
        
for i in range(1,N+1):
    print(basket[i], end=" ")