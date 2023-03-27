N = int(input())

# 증가 별 출력
for i in range(N):
    # 공백 출력
    for j in range(N-1-i):
        print(" ", end="")
    # 별 출력
    for k in range(2*i+1):
        print("*", end="")
    print()
    
# 감소 별 출력
for i in range(N-1):
    # 공백 출력
    for j in range(1+i):
        print(" ", end="")
    # 별 출력
    for k in range(2*N-3-2*i):
        print("*", end="")
    print()