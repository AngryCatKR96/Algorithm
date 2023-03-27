def gcd(num1, num2):
    while num2 != 0:
        left = num1 % num2
        num1 = num2
        num2 = left
    
    return num1

A, B = map(int, input().split())


if A > B:
    print(A*B//gcd(A,B))
else:
    print(A*B//gcd(B,A))
    