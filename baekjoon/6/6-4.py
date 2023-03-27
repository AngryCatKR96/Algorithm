T = int(input())

list = []

for i in range(T):
    result = ""
    R, S = input().split()
    R = int(R)
    
    for j in range(len(S)):
        result = result + S[j]*R
        
    list.append(result)
        
for i in range(T):
    print(list[i])
    
    
    

