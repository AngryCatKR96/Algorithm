n = int(input())

final = []

for i in range(n):
    score = 0
    result = 0
    
    OX = input()
    
    for j in range(len(OX)):
        if OX[j] == "O":
            score += 1
            result += score
        else:
            score = 0
            
    final.append(result)
    
for i in range(n):
    print(final[i])
    
    
    
