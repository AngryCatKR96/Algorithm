"""
문제 요약 - 한번 입었던 옷들의 조합을 절대 다시 입지 않는 해빈이가 가진 옷들만으로 알몸이 아닌 상태로 
며칠동안 밖에 돌아 다닐 수 있는지 묻는 문제
의상의 이름, 의상의 종류가 주어지며 같은 의상의 종류는 함께 입을 수 없으므로
각 의상의 종류를 하나씩만 입어서 입을수 있는 경우의 수
문제 핵심 - 중복을 제거하는 것이 포인트
총 n종류의 의상이 있고 각 의상의 종류를 ki(i는 1이상 n이하의 자연수) 이 때, 의상을 적어도 한개 이상 고르는 경우의 수는
(2**n-1)*k1*k2*...*kn - (2**(n-1)-1)*(k1-1)*(k2-1)*...*(kn-1) 이다. 이를 구현하라
"""
import sys

# 테스트케이스 수 T 입력
T = int(input())
# T회 만큼 테스트케이스 입력
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    
    # 의상 종류를 key로, value는 count값
    clothes = dict()
    for _ in range(N):
        name, kind = sys.stdin.readline().strip().split()
        if kind not in clothes:
            clothes[kind] = 2
        else:
            clothes[kind] += 1
            
    # k를 뽑아내기 위해 value로만 이루어진 list를 만듬
    Ks = list(clothes.values())

    # 계산 전 초기화
    case = 1
    # case 계산
    for i in range(len(Ks)):
        case *= Ks[i]
        
    # case - over 출력
    print(case - 1)