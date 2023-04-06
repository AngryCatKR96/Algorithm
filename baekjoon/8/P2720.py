T = int(input())

for _ in range(T):
    change = int(input())
    
    Q = change // 25
    change %= 25
    
    D = change // 10
    change %= 10
    
    N = change // 5
    change %= 5
    
    P = change
    
    print(Q, D, N ,P)
    