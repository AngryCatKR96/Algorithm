import sys

A, B, V = map(int,sys.stdin.readline().split())

diff = V-A
climb = A-B
max = int(V/climb)
ggodari =  V-max*climb

N=1

while ggodari + climb*N < A:
    N += 1
    
gap = ggodari + climb*(N-1)

if diff%climb == 0: # 마지막 일 낮에 딱 맞게 도착하는 경우
    result = diff/climb + 1 
else: 
    result = max-int(gap/climb)+1

print(int(result))