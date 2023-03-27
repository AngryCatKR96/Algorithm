import sys

# N 입력
N = int(sys.stdin.readline().strip())

# 리스트에 저장
inputList = [["" for col in range(2)] for row in range(N)]
for i in range(N):
    inputList[i][0] = sys.stdin.readline().strip()
    inputList[i][1] = len(inputList[i][0])
    
        
    

# 길이로 정렬
inputList.sort(key= lambda x : (x[1], x[0]))


# 출력
for i in range(N):
    if i!=0 and inputList[i][0] == inputList[i-1][0]:
        continue
    print(inputList[i][0])