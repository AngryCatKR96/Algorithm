"""각 변까지의 거리를 모두 구해서  최솟값을 구하자"""

x, y, w, h = map(int,input().split())

print(min(x,y,h-y,w-x))
