"""브루트 포-스로 해결 가능하므로 N보다 작은수를 -1씩 해가며 찾고 그 수의 각 자릿수의 합이 N과 같은지 체크(if문)
언제까지? M이 1이 될때까지 => 없으면 0출력"""
N = int(input())

M = 1
min = 0
while(M<N):
    # M의 자릿수 더하기
    K = M
    sum = 0
    while (K>0):
        sum += K%10
        K = K//10   
    # 생성자면 탈출
    if(M+sum == N):
        break
    # 생성자 아니면 +1
    M += 1

if(M==N):
    print(0)
else:
    print(M)
        