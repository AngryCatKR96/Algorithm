import sys

# update, 원본배열과 트리 업데이트, 업데이트할 index와 업데이트할 값을 매개변수로 받는다. dif만큼 더하는 함수, void
def update(i, dif):
    while i <= N:
        binaryIndexTree[i] += dif # 트리의 원래 값에 dif만큼 더 해주는데
        i += (i & -i) # i번째 값을 포함하는 모든 index에도 반영해주어야하므로 0이 아닌 마지막 비트만큼 더하면서 구간들의 값을 변경

# prefix_sum(누적합) 구하는 메서드, return result
def prefix_sum(i):
    result = 0
    while i > 0:
        result += binaryIndexTree[i] # 결과에 트리의 값을 더해주는데 트리의 값이 누적합은 아니므로
        i -= (i & -i) # 0이 아닌 마지막 비트만큼 빼면서 구간들의 값의 합 계산
    return result

# interval_sum(구간합) 구하는 메서드
def interval_sum(start , end):
    return prefix_sum(end) - prefix_sum(start-1)

N, M , K = map(int, input().split())

arr = [0 for _ in range(N+1)] # 원본 배열
binaryIndexTree = [0 for _ in range(N+1)] # 2진법 인덱스 구조를 활용한 바이너리 인덱스 트리

# 원본 배열 입력
for i in range(1,N+1):
    num = int(sys.stdin.readline().strip())
    arr[i] = num # 원본 배열에도 넣고
    update(i, num) # tree에도 반영해준다.
    
for _ in range(M+K):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    
    if a == 1:
        update(b, c-arr[b]) # 차이만큼 더 해주는 것이므로 update(b,c)가 아닌 원래 값과 c의 차이를 더해줘야한다
        arr[b] = c # 순서 주의! 업데이트하고 arr에 넣어야함. 
    else:
        print(interval_sum(b,c))
