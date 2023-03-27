# 나이, 이름을 2차원 리스트에 저장하고 세번째 요소는 가입 순서로 한다.
# 나이 -> 가입 순서 순으로 정렬
# 출력은 나이 이름
import sys

N = int(sys.stdin.readline().strip())

list = [[0 for _ in range(3)] for _ in range(N)]
for i in range(N):
    age, name = sys.stdin.readline().strip().split()
    list[i][0] = int(age)
    list[i][1] = name
    list[i][2] = i

list.sort(key= lambda x : (x[0],x[2]))

for i in range(N):
    print(list[i][0], end=" ")
    print(list[i][1])