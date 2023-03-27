import sys

# x를 기준으로 정렬, x가 같으면 y를 기준으로 정렬
# 버블 정렬, xy좌표
def bubbleSort(input_list):
    temp = 0
    for i in range(0,len(input_list)-1): # 제외될 원소의 갯수
        for j in range(0,len(input_list)-1-i): # 비교할 list의 범위
            # x 좌표 비교 
            if input_list[j][0] > input_list[j+1][0]: 
                # x좌표 스왑
                input_list[j][0], input_list[j+1][0]  = input_list[j+1][0], input_list[j][0]
                # y좌표 스왑
                input_list[j][1], input_list[j+1][1]  = input_list[j+1][1], input_list[j][1]
            # x 좌표 같을 때 
            elif input_list[j][0] == input_list[j+1][0]:
                # y 좌표 비교 
                if input_list[j][1] > input_list[j+1][1]: 
                    # x좌표 스왑
                    input_list[j][0], input_list[j+1][0]  = input_list[j+1][0], input_list[j][0]
                    # y좌표 스왑
                    input_list[j][1], input_list[j+1][1]  = input_list[j+1][1], input_list[j][1]

    return input_list

# N 입력
N = int(sys.stdin.readline().strip())

list = [[0 for col in range(2)] for row in range(N)]
# 2차원 리스트에 저장
for i in range(N):
    list[i][0], list[i][1] = map(int,sys.stdin.readline().strip().split())

# 정렬
bubbleSort(list)

# 출력
for i in range(N):
    print(list[i][0], end=" ")
    print(list[i][1])