import sys

input = sys.stdin.readline

count = 0

Num = input().strip()

if len(Num) == 1:
    FirstNum = "0" + Num
else: 
    FirstNum = Num
    

while True:
    count += 1
    
    if len(Num) == 1:
        Num = "0" + Num
        
    SumNum = int(Num[0]) + int(Num[1])
    SumNum = str(SumNum)

    if len(SumNum) == 1:
        SumNum = "0" + SumNum
        
    Num = Num[1] + SumNum[1]
    
    if FirstNum == Num:
        print(count)
        break

    
    
    
        

