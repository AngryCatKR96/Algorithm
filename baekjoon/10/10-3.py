# 커트라인 = 상을 받는 사람들 중 점수가 가장 낮은 사람의 점수
# 결국 정렬 문제, 내림차순으로 정렬해서 k번째 사람의 점수를 찾자

# 삽입 정렬 메서드
def insertionSort(list):
    prev = 0
    temp = 0
    for index in range(1,len(list)):
        temp = list[index]
        prev = index - 1
        while prev >= 0 and temp < list[prev]:
            list[prev+1] = list[prev]
            prev -= 1
        list[prev+1] = temp
    return list

# N, k 입력
N, k = map(int,input().split())

# N개만큼 x 입력
scores = list(map(int,input().split()))
    
# 정렬 메서드 실행
insertionSort(scores)

# k번째 점수 출력
print(scores[N-k])