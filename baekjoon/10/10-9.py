import sys

# N 입력
N = int(sys.stdin.readline().strip())

list = [[0 for col in range(2)] for row in range(N)]
# 2차원 리스트에 저장
for i in range(N):
    list[i][1], list[i][0] = map(int,sys.stdin.readline().strip().split())

# 정렬
list.sort()

# 출력
for i in range(N):
    print(list[i][1], end=" ")
    print(list[i][0])