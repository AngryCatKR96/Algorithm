"""재귀, base condition은? 원판이 하나일 때, 일반항은 젤큰거 뺀 나머지를 임시로 옮기고 + 젤 큰거 목표로 옮기고 + 나머지 목표로 옮기고"""
def hanoi(num, start, by, end):
    global count
    global result
    if(num==1):
        #print(start, end)
        result.append([start,end])
        count += 1
        return
    
    hanoi(num-1, start, end, by)
    result.append([start,end])
    #print(start, end)
    hanoi(num-1, by, start, end)
    count += 1

N = int(input())

count = 0
result = []

hanoi(N, 1, 2, 3)

print(count)
for i in range(len(result)):
    print(result[i][0], result[i][1])