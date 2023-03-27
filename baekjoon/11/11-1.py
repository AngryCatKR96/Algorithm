import sys

def facto(N):
    if N == 0:
        return 1
    return facto(N-1)*N

N = int(sys.stdin.readline().strip())

print(facto(N))