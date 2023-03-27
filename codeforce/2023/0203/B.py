import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    moves = sys.stdin.readline().strip()
    
    posX = 0
    posY = 0    

    count = False
    
    for i in moves:
        if i == 'L':
            posX-=1
            if (posX==1 and posY==1):
                print("YES")
                count=True
                break
        elif i == 'R':
            posX+=1
            if (posX==1 and posY==1):
                print("YES")
                count=True
                break
        elif i == 'U':
            posY+=1
            if (posX==1 and posY==1):
                print("YES")
                count=True
                break
        elif i == 'D':
            posY-=1    
            if (posX==1 and posY==1):
                print("YES")
                count=True
                break
            
    if(count==False):
        print("NO")   


