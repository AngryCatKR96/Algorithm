import sys

T = int(sys.stdin.readline())

result  = []

for _ in range(0,T):
    H, W, N = map(int,sys.stdin.readline().split())
    
    floor = N%H
    hosu =  N//H+1
    if floor == 0:
        floor = H
        hosu = N//H
    
    if hosu < 10: 
        room = str(floor)+ "0" +str(hosu)
    else:
        room = str(floor) +str(hosu)
    result.append(room)
    
for i in result:
    print(i)

    
    