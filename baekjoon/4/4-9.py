ratios = []

C = int(input())

for i in range(C):
    scores = list(map(int,input().split()))
        
    avg = sum(scores[1:])/(scores[0])
    
    students = 0
    for k in scores[1:]:
        if k > avg:
            students += 1
            
    ratio = students/scores[0]*100
    ratios.append(ratio)
    
for i in range(C):
    print("%0.3f%%" % ratios[i])
    
    
    
    