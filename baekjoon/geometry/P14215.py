a, b, c = map(int, input().split())

lenList = [a,b,c]
lenList.sort()

if lenList[0] + lenList[1] > lenList[2]:
    print(sum(lenList))
else:
    lenList[2] = lenList[0] + lenList[1] - 1
    print(sum(lenList))
 