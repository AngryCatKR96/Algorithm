"""두 원의 교점을 구하는 문제, 두 원의 중심간의 거리 == 두 원의 반지름길이의 합 이면 한점에서 만나므로 1
거리 > 합 이면 0, 거리< 합 이면 2, 중심이 같고 반지름 크기 같으면 -1, 반지름 크기 다르면 """
import math

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    
    if x1 == x2 and y1 == y2 and r1 == r2: # 겹치는 원
        print(-1)
    elif x1 == x2 and y1 == y2 and r1 != r2: # 동심원인데 반지름 다름
        print(0)    
    else:
        dist = math.sqrt(pow(x1-x2,2) + pow(y1-y2,2))
        if dist == abs(r1-r2): #내접
            print(1) 
        elif dist  < max(r1,r2) and dist < abs(r1-r2): # 안에서 안만남
            print(0)
        elif dist  < max(r1,r2) and dist > abs(r1-r2): # 안에서 두점
            print(2)
        elif dist == r1 or dist == r2: # 한 원의 중심이 다른 원 위에 있음
            print(2)
        elif dist == r1+r2: # 외접
            print(1) 
        elif dist > r1+r2: # 밖에서 안만남
            print(0)
        elif dist < r1+r2: # 밖에서 두점
            print(2)
        
        
    