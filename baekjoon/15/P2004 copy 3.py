# n!안에 k의 몇제곱이 들어있는지 확인하는 함수
def count_expon(n, k):
    # 변수 초기화
    count = 0
    div = k
    # n보다 작거나 같은 k의 제곱들로 나눠서 n!안에 k의 몇제곱이 들어있는지 확인
    while n >= div:
        count += n // div
        div *= k
        
    return count
        
N, M = map(int,input().split())


# 10의 몇승이 들어있는지 확인 > 2와 5이 몇승인지 확인해서 그 중 작은 수가 10의 개수
count5 = count_expon(N,5) - count_expon(M,5) - count_expon(N-M,5)
count2 = count_expon(N,2) - count_expon(M,2) - count_expon(N-M,2)

print(min(count2,count5))