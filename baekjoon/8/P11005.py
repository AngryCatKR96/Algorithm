def convert(n, b):
    T = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    q, r = divmod(n, b)
    
    return convert(q, b) + T[r] if q else T[r]

N, B = map(int,input().split())

print(convert(N,B))