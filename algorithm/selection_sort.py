# 수열을 list로 받는다
# 최소값을 찾는다 = index값 이용해서 하나하나 비교해가며 더 작은 값이 있으면 새로 index에 저장하는 식으로
# 최소값을 첫 번째 요소와 교체
# 첫번째 요소 정렬에서 제외하고 두번째 요소부터 동일하게 반복

def selection_sort(list):
    min, index_Min = 0 # 변수 정의 ; index는 최솟값, index_Min는 최솟값이 나온 위치
    for i in range(0,len(list)-1): # 정렬 제외할 범위를 선택해준다
        min = list[i] # 항상 스타트는 맨앞부터
        index_Min = i
        for j in range(i,len(list)-1): # 정렬제외한 위치부터 끝까지 비교
            if min > list[j+1]: # 비교를해서 작으면 값을 갱신해준다
                min = list[j+1]
                index_Min = j+1
        list[i], list[index_Min]  = min, list[i] # 한 사이클을 돌린 뒤 최종적으로 최솟값을 맨 앞의 값과 바꿔줌
        
    return list

N = list(map(int,input().split()))

print(selection_sort(N))