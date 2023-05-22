import sys
input = sys.stdin.readline

# 이진 탐색 메서드
def binarySearch(array, x):
    start = 0
    end = len(array) - 1
    mid = (start + end) // 2
    
    while(start <= end):
        mid = (start + end) // 2
        
        if x == array[mid]:
            return 1
        elif x < array[mid]:
            end = mid - 1
        elif x > array[mid]:
            start = mid + 1
    return 0 

# N 입력 받기
N = int(input())

# N개의 정수 입력 받기
arr = list(map(int,input().split()))

# 정렬
arr.sort()

# M 입력 받기
M = int(input())

# M개의 수 입력 받기
nums = list(map(int,input().split()))

# 이진 탐색 실행
for num in nums:
    print(binarySearch(arr, num))