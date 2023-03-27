"""상근이가 중복을 허용하는 카드 N개를 갖고 있고 각 수에 해당하는 숫자카드를 몇개 갖고 있는지 출력하는 문제
일반 중복을 허용하므로 set은 못쓴다. 갯수만 세면되니까 counting sort에서 쓰던 스킬을 그대로 쓰면되지 않을까?
6이 들어오면 count list의 6 index의 값을 1 증가 시켜주는거지 그렇게하고 M에 대해서는 각 인덱스의 값을 출력해주기만 하면 되니까
아 근데 음수도 있구나... 음수용 양수용 두개 만들어야겠다."""
import sys

#입력
N = int(input())
cards = list(map(int,sys.stdin.readline().strip().split()))
M = int(input())
targets = list(map(int,sys.stdin.readline().strip().split()))

# 카운팅 리스트 생성
countPlus = [0]*10000001
countMinus = [0]*10000000

# cards 이용해서 카운팅 리스트 채우기
for card in cards:
    if card >= 0:
        countPlus[card] += 1
    else:
        countMinus[card] += 1

# targets에 있는 수 카운팅 리스트에서 값 찾기 & 값 저장
result = []
for i in targets:
    if i>=0:
        print(countPlus[i], end=" ")
    else:
        print(countMinus[i], end=" ")