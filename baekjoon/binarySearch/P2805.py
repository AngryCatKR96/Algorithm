""" 절단기의 높이 h가 이분탐색의 기준이 될 거야. 상근이가 적어도 M미터를 집으로 가져가기 위한 절단기의 높이 h의 최댓값을 구하자!  """
import sys 
input = sys.stdin.readline

# N, M 입력 받기
N, M = map(int, input().split())

# N개의 나무 높이 입력 받기
trees = list(map(int,input().split()))
maxHeight = max(trees)

# 0부터 가장 키가 큰 나무의 높이를 범위로 이분 탐색을 실시하는 메서드, 이번에는 list를 반환하는 것이 아닌 높이의 최댓값을 반환하도록 해보자
def paraSearch(inputList, inputMax, inputObject):
    # 변수 초기화
    result = []
    start = 0
    end =  inputMax
    
    # 반복문으로 이분탐색 실행
    while start <= end:
        mid = (start + end) // 2 # mid가 절단기의 높이 h
        
        # 상근이가 집에 가져가는 나무 길이 구하기
        lenTree = 0
        for t in inputList:
            if t - mid > 0:
                lenTree += t - mid
                
        # 나무의 길이가 조건에 부합하는지 검사
        if lenTree >= inputObject:
            result.append(mid)
            start = mid + 1
        else:
            end = mid - 1
    
    return max(result)

# 출력
print(paraSearch(trees, maxHeight, M))