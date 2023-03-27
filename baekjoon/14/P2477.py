"""참외밭의 넓이만 구하면 되는 문제, 일단 참외밭의 형태는 무조건 ㄱ자 형이다(방향은 바뀔 수 있음) 
방향을 주면서 길이를 주는데 시작점이 임의의 점이므로 시작점에 관계없이 넓이를 구하는 방법을 생각해내야한다.
뭔가 규칙성이 있을 것이다!!
가장 큰 변의 길이는 방향의 개수로 찾는다
방향이 반시계니까 4->2->3->1->4...이런식으로 반복되는데 이 반복에서 벗어날 때 그 변과 그 전의 변이 작은 네모를 가르킨다
근데 시작이 벗어나는 변이면?? 그땐 제일 처음과 제일 마지막 변이 작은 네모의 변이다 
"""
# K 입력
K = int(input())
# 방향 순서 리스트 생성 및 초기화
ccw = [4,2,3,1]
# 방향순서의 위치를 저장해주는 변수 선언
pointer = 0
# 6번 입력 받기
dir = []
dis = []
for i in range(6):
    R, S = map(int,input().split())
    dir.append(R)
    dis.append(S)
# 개수가 하나인 방향의 변이 큰 네모의 두 변
big = []
for i in range(1,5):
    if dir.count(i) == 1:
        big.append(dis[dir.index(i)])

# 작은 네모 찾기
small = []
pointer = ccw.index(dir[0])
count = 0
for i in range(6):
    # 방향에서 벗어나면 그게 작은 네모
    if dir[i] == ccw[pointer]:
        count += 1
        pointer+=1
        if pointer == 4:
            pointer = 0
    else:
        small.append(dis[i-1])
        small.append(dis[i])
        break
    
# 벗어난 적이 없으면 가장 처음과 마지막의 변이 작은 네모
if count == 6:
    small.append(dis[0])
    small.append(dis[5])

    
print(K*(big[0]*big[1] - small[0]*small[1]))

