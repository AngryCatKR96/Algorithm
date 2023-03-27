import sys

# 개수 N
N = int(sys.stdin.readline().strip())

# 입력
list = []
for _ in range(N):
    list.append(int(sys.stdin.readline().strip()))

# 정렬
list.sort()

 # 출력
for i in list:
    print(i)