"""N개의 수를 M으로 나누었을 때 나머지가 모두 같은 M을 찾는 문제
일단 간단하게 생각하면 브루트 포스로 풀면된다. N개의 수를 2부터 1씩 증가시키며 가장 작은 수보다 작은 수까지 나눠본다.
최악의 경우 100개의 1,000,000,000이 주어질수 있으므로 시간 초과가 날 거 같다. >> 그래도 일단 해보자
역시 브루트 포스는 시간 초과가 뜨네... 다른 로직을 생각해보자
규칙을 찾아내야한다!!
6 36 216이 있을 때 37,38.. 등을 모두 검사할 필요가 없는게 어차피 3보다 큰 수로 6을 나누면 뭘로 나누던 6이 나오기 때문에 나머지 수를
M으로 나눴을 때 나머지가 6이 되는 M만 찾으면된다 >> 최솟값이 중요하다라는 말
M은 두번째로 작은수-최솟값보다 커질수없다. 나머지가 6이 되어야하는데 30보다 커지는 순간 나머지가 6이 안되기 때문에
결국 최솟값을 제외한 나머지 값들에서 최솟값을 뺀 값들의 최대공약수를 구하고 그 최대 공약수의 약수(1 제외)가 정답이 된다.
"""
import sys, math
# 최대공약수 구하는 메서드
def GCD(num1, num2):
    rem = num1 % num2
    while rem != 0:
        num1 = num2
        num2 = rem
        rem = num1 % num2
        
    return num2
# 약수 구하는 메서드
def aliquot(num):
    result = []
    for i in range(1,int(math.sqrt(num))+1):
        if num % i == 0:
            result.append(i)
            result.append(num//i)
    
    return sorted(list(set(result)))

N = int(sys.stdin.readline().strip())

inputList = []
for _ in range(N):
    inputList.append(int(sys.stdin.readline().strip()))
    

inputList.sort()
m = inputList[0] # 가장 작은 값

# M 구하기
# 최솟값을 모두 빼 줌
for i in range(len(inputList)):
    inputList[i] -= m
    
# inputList 길이 2일 때
if len(inputList) == 2:
    result = aliquot(inputList[1])
# inputList 길이 3일 때
elif len(inputList) == 3:
    result = aliquot(GCD(inputList[1],inputList[2]))
# inputList 길이 4 이상일 때
else:
    gcd = GCD(inputList[1],inputList[2])
    for i in range(3,len(inputList)):
        gcd = GCD(inputList[i],gcd)
        
    result = aliquot(gcd)


for i in range(1,len(result)):
    print(result[i], end= " ")

