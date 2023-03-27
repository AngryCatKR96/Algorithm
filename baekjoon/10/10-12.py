# 좌표 압축
# 각 수보다 작은 수가 몇개 있는지를 구하는 문제
# 메모리는 넉넉하나 시간이 2초라 시간복잡도를 고려할 것
# 정렬은 그냥 하면되는데 중요한건 중복과 출력
# 출력시에 입력된 순서 그대로 출력해야 하므로 입력된 순서를 저장해두는 것이 필요하다
import sys 

N = int(sys.stdin.readline().strip())
inputList = list(map(int,sys.stdin.readline().strip().split()))

list = [[0 for _ in range(2)] for _ in range(N) ]
for i in range(N):
    list[i][0] = inputList[i]
    list[i][1] = i

list.sort()

resultList = [0]*N
for i in range(N):
    if i > 0 and list[i][0] == list[i-1][0]:
        resultList[list[i][1]] = resultList[list[i-1][1]]
    elif i > 0 and list[i][0] != list[i-1][0]:
        resultList[list[i][1]] = resultList[list[i-1][1]] + 1
    else:
        resultList[list[i][1]] = 0
        
for i in resultList:
    print(i, end=" ")