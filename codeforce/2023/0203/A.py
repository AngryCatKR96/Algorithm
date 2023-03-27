t = int(input())

string = "codeforces"

for _ in range(t):
    c = input()
    if(string.find(c) != -1):
        print("YES")
    else:
        print("NO")
        