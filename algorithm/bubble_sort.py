# 수열을 input(list) 받아서 거품 정렬을 이용해 정렬한 뒤 ouput으로 내보내주는 함수를 만들자
# 0,1 번째 요소를 비교하고 조건에 맞는지 보고 결과에 따라 위치를 바꿔준 뒤
# 1, 2번째 요소도 동일하게 반복
# 쭉 해서 n-1번째 요소와 n번째 요소를 비교한다
# 이러면 1회전 끝! 그리고 n째 요소를 정렬에서 제외하고 n-1번째 요소까지 동일하게
# 사이클 반복
# 이것을 1,2번째 요소만 비교하게 될때까지 반복!

def bubble(input_list):
    temp = 0
    for i in range(0,len(input_list)-1): # 제외될 원소의 갯수
        for j in range(0,len(input_list)-1-i): # 비교할 list의 범위
            if input_list[j] > input_list[j+1]: # 비교 과정
                temp = input_list[j]
                input_list[j] = input_list[j+1]
                input_list[j+1] = temp
    return input_list
        
N = list(map(int,input().split()))

print(bubble(N))        
        