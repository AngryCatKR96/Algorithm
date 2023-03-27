"""행성계 진입에 필요한 최소한의 횟수 >> 무슨 의미일까? 실제로 곡선을 그리는건 불가능 > 분명 다른 해석법이 존재할것이다
피할 수 없는 행성과 피할 수 있는 행성의 차이가 뭐지?? 출발점이나 도착점을 원안에 포함하고있는 원의 개수를 세라?
포함 << 원의 중심과 도착or출발점 사이의 거리가 해당 원의 반지름보다 작다
단순히 포함관계만으로는 정답이 될 수 없다.
점은 이미 주어지고 >> 원을 하나씩 확인한다고 할 때
한점만 포함하고 있고 다른 점은 포함하고 있지 않을 때 >> 카운터 해줌
"""
import math

T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int,input().split())
    N = int(input())
    
    count = 0
    for _ in range(N):
        cx, cy, r = map(int,input().split())
        
        dist1 = math.sqrt(pow(x1-cx,2) + pow(y1-cy,2))
        dist2 = math.sqrt(pow(x2-cx,2) + pow(y2-cy,2))
        
        if dist1 < r and dist2 > r:
            count += 1
        if dist1 > r and dist2 < r:
            count += 1
            
    print(count)
