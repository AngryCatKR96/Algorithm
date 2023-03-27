N, M = map(int,input().split())

mat1 = []
mat2 = []
mat3 = []

for i in range(N):
    mat1.append(list(map(int,input().split())))
for i in range(N):
    mat2.append(list(map(int,input().split())))
    
for i in range(N):
    row = []
    for j in range(M):
        row.append(mat1[i][j] + mat2[i][j])
    mat3.append(row)    
        
for i in range(N):
    for j in range(M):
            print(mat3[i][j],end=" ")
    print()