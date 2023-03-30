import sys
input = sys.stdin.readline


N, M = map(int, input().split())
    
# 바구니 초기화
bagunis = []
for i in range(N):
    bagunis.append(i+1)

for _ in range(M):
    begin, end, mid = map(int, input().split())
    begin -= 1
    mid -= 1
    end -= 1
    
    before = bagunis[0:begin]
    #print(before)
    a = bagunis[begin:mid]
    #print(a)
    b = bagunis[mid:end+1]
    #print(b)
    after = bagunis[end+1:]
    #print(after)
    
    bagunis.clear()
    bagunis = before + b + a + after

for i in range(N):
    print(bagunis[i], end=" ")
    
    