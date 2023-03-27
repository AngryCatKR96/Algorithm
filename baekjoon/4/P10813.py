import sys

N, M = map(int,input().split())

# 처음 바구니 생성
basket = []
for i in range(1,N+1):
    basket.append(i)

# M번 교환
for _ in range(M):
    i, j = map(int,sys.stdin.readline().strip().split())
    
    #swap
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]
    
# 바구니 출력
for i in basket:
    print(i, end=" ")