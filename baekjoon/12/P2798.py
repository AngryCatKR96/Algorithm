"""모든 경우의 수를 더해봐야함. for문 세번 사용해서 세개 고르면 될듯?"""
import sys

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

max = 0
for i in range(len(numbers)-2):
    for j in range(i+1,len(numbers)-1):
        for k in range(j+1,len(numbers)):
            sum = numbers[i]+numbers[j]+numbers[k]
            if(sum<=M and sum>max):
                max = sum
                
print(max)