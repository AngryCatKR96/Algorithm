N, M = 9, 9
mat = []
MaxList = []

for i in range(N):
    mat.append(list(map(int,input().split())))

for i in range(N):
    MaxList.append(max(mat[i]))

MaxNum = max(MaxList)

for i in range(N):
    try:
        n = i+1
        m = mat[i].index(MaxNum) +1
        break
    except:
        pass

print(MaxNum)
print(n,end=" ")
print(m)
        