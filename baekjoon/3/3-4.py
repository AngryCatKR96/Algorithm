total = int(input())
test = int(input())

price = 0

for i in range(test):
    A, B = map(int,input().split())
    price = price + A*B
    
if price == total:
    print("Yes")
else:
    print("No")

