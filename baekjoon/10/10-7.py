import sys

# 연속된 수를 자리수를 이용해 입력받는 방법
N = sys.stdin.readline().strip()
intN = int(N)

# 정렬이니 결국엔 리스트에 저장해야함, append가 메모리를 많이 쓴다고?
list = [0]*len(N)
for i in range(len(N)):
    list[i] = intN % 10
    intN = int(intN/10)
    
# 정렬
list.sort(reverse=True)

# 출력
for i in list:
    print(i, end="")