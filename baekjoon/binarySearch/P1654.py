""" K개의 랜선이 있고 최소 N개의 랜선을 만들어야하는구나. 이 때 만들수 있는 랜선의 최대 길이를 구하는 문제군! 최소와 최대에 집중을 한번 해볼까?
만들고 싶은 랜선의 길이를 x로 두고 랜선의 길이가 증가하면 만들 수 있는 랜선의 개수는 줄어들겠지
증가하다보면 결국엔 (최대)에 도달할거고 그럼 개수의 (최소)에 도달하겠군! 이렇게 최대와 최소가 연관이 있구나
결국엔 랜선의 길이를 고르고 -> 조건(개수)에 맞는지 검사하고 -> 아니면 다시 고르고의 과정을 거쳐야하는데
랜선의 길이 x의 범위가 매우 넓어서 시간만족도를 충족시키기 위해서는 이분 탐색을 써야하는 문제로군!"""
import sys

input = sys.stdin.readline

# K, N 입력 받기
K, N = map(int,input().split())

# 랜선 K개 입력 받기
LANs = []
for _ in range(K):
    LANs.append(int(input()))

maxLen = max(LANs)
# 가장 긴 랜선의 길이를 기준으로 랜선의 최대 길이를 이분 탐색으로 찾는 메서드
def parametricSearch(inputList, inputMax, object):
    result = []
    start = 1 # 스타트가 0이어야할까 1이어야 할까?
    end = inputMax
    
    while start <= end:
        mid = (start + end) // 2 # mid가 자르고 싶은 길이
        
        # 조건에 부합하는지 검사
        count = 0
        for i in range(len(inputList)):
            count += inputList[i] // mid
        
        # if count == object: # 랜선의 개수가 목표 개수와 같다면 조건에 부합하므로 결과를 저장한다
        #     start = mid + 1
        #     result.append(mid)
        if count < object: # 랜선의 개수가 목표 개수보다 적다면 길이가 너무 긴 것이므로 앞의 절반의 범위로 줄여준다
            end = mid - 1
        else: # 랜선의 개수가 목표개수보다 크거나 같다면 랜선의 길이가 일단 조건에는 부합하므로 결과를 저장해둔다
            start = mid + 1
            result.append(mid)
            
    return result

# 메서드 실행
print(max(parametricSearch(LANs, maxLen, N)))
