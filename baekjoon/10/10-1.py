# 수정렬하기, 절댓값이 1000보다 작거나 같은 정수.
# 시간 복잡도가 O(n^2)인 정렬 알고리즘으로 풀 수있음. 삽입or거품
# 오름차순으로!

# 정렬 알고리즘 메서드, Bubble Sort
def sort(list):
    for i in range(len(list)-1):
        for j in range(0,len(list)-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
            else:
                continue
    return list

# 변수 선언
listSort = []

# N 입력
N = int(input())


# N개의 수 입력, for문 이용, 리스트에 저장
for _ in range(N):
    listSort.append(int(input()))
    
# 정렬 메서드 실행, 정렬한 리스트 저장
sort(listSort)

# for문 이용해서 정렬한 리스트 출력
for i in listSort:
    print(i)