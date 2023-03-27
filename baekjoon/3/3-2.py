test = int(input())
numbers = []

for i in range(test):
    A, B = input().split()
    numbers.append([A,B])

for i in range(test):
    print(int(numbers[i][0]) + int(numbers[i][1]))