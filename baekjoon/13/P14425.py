import sys

# 입력
N, M = map(int,input().split())

S = set()
for _ in range(N):
    S.add(sys.stdin.readline().strip())
    
test = []
for _ in range(M):
    test.append(sys.stdin.readline().strip())
# in으로 있는지 없는지 확인 있으면 count +1
count = 0
for word in test:
    if word in S:
        count += 1
        
print(count)