# 대표값2
# 평균은 평범하게 계산하면 되고 중앙값은 결국 정렬을 해야하는데 정렬 방법은 10-1에서 거품 정렬을 사용했으니까 
# 이번에는 선택 정렬을 사용해보자! 자주 연습할 수록 강해진다

# 선택정렬 메서드
def SelectionSort(list):
    for i in range(len(list)-1):
        minValue = list[i]
        minIndex = i
        for j in range(i, len(list)-1):
            if list[j+1] < minValue:
                minValue = list[j+1]
                minIndex = j+1
        list[i], list[minIndex] = list[minIndex], list[i]
                
    return list

# 변수 선언
listSort = []
sum = 0

# 5개의 입력 받고 리스트에 저장
for _ in range(5):
    listSort.append(int(input()))
    
# 리스트 정렬
SelectionSort(listSort)

# 평균 계산
for i in listSort:
    sum += i

# 출력
print(int(sum/5))
print(listSort[2])