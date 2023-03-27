import sys

N = int(input())

stack = list()

for _ in range(N):
    command = sys.stdin.readline().strip()

    if command == "pop":
        try:
            print(stack.pop())
        except:
            print(-1)
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        if(len(stack)==0):
            print(1)
        else:
            print(0)
    elif command == "top":
        try:
            print(stack[-1])
        except:
            print(-1)
    else:
        C, X = command.split()
        stack.append(int(X))
        