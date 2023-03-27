"""최대 판매 수익을 구하는 문제
인당 한개밖에 못팜. 달걀을 전부 다 안팔아도됨. 많이 판다고 좋은게 아님!
싼 가격에 다 팔아도 높은 가격에 덜파는게 오히려 더 많은 수익을 남길 수도 있음
최대판매니까 높은 가격부터 찾는게 빠를까 낮은 가격부터 찾는게 빠를까 >> 상황따라 다르지 않을까
사람이 달걀 개수보다 많을 때도 생각해야함. >> 달걀 다 파는 경우의 수 중에선 최대값부터 5명 고르는게 가장 수익 많음
따라서 얼마나 리스트가 길어지던간에 무조건 5번만 검사하면됨!
"""
# 입력
N, M = map(int, input().split())

buyer = []
for _ in range(M):
    buyer.append(int(input()))

# 정렬    
buyer.sort()

# 최대수익 찾기 
if(M>=N):
    price = buyer[-N]
    revenue = price*N
    for i in range(1,N+1):
        if(buyer[-N-1+i]*(N+1-i) > revenue):
            price = buyer[-N-1+i]
            revenue = price*(N+1-i)
else:
    price = buyer[-M]
    revenue = price*M
    for i in range(1,M+1):
        if(buyer[-M-1+i]*(M+1-i) > revenue):
            price = buyer[-M-1+i]
            revenue = price*(M+1-i)
        
print(price, revenue)