import sys

N = int(sys.stdin.readline().strip())

list = []
sum = 0
plusCounter = [0]*500001
minusCounter = [0]*500001
for i in range(N):
    temp = int(sys.stdin.readline().strip())
    list.append(temp)
    sum += temp
    if temp >= 0:
        plusCounter[temp] += 1
    else:
        minusCounter[-temp] += 1
    
list.sort()

listMaxCount = []
plusMaxCount = max(plusCounter)
minusMaxCount = max(minusCounter)

if plusMaxCount > minusMaxCount:
    maxCount = plusMaxCount
    for i in range(500001):
        if maxCount == plusCounter[i]:
            listMaxCount.append(i)
elif plusMaxCount < minusMaxCount:
    maxCount = minusMaxCount
    for i in range(500001):
        if maxCount == minusCounter[i]:
            listMaxCount.append(-i)
            listMaxCount.sort()
else:
    maxCount = plusMaxCount
    for i in range(500001):
        if maxCount == minusCounter[i]:
            listMaxCount.append(-i)
            listMaxCount.sort() 
            
    for i in range(500001):
        if maxCount == plusCounter[i]:
            listMaxCount.append(i)

# 출력
# 산술평균
print(int(round(sum/N,0)))
# 중앙값
if N%2 != 0:
    print(list[N//2])
else:
    print((list[N//2]+list[N//2+1])/2)
#최빈값
if len(listMaxCount) == 1:
    print(listMaxCount[0])
else:
    print(listMaxCount[1])
# 범위
print(list[N-1] - list[0])

    