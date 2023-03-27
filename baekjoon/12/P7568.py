"""브루트 포스 -> 모든 경우의 수 비교, 사람 한명 골라서 -> 자신을 제외한 모든 사람과 비교 -> 몇명이 자기보다 덩치가 큰지 카운트
카운트 +1이 등수"""
# 입력
N = int(input())

people = []
for _ in range(N):
    people.append(list(map(int,input().split())))

result = []
# 비교(자기 포함해도 비교해도 어차피 COUNT안되니까 괜찮을듯)
for i in range(N): # 비교 기준 선택
    count = 0
    for j in range(N): # 돌아가면서 비교
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            count += 1
    result.append(count+1)

# 출력
for i in range(N):
    print(result[i], end=" ")