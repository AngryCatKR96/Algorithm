import sys

def merge_sort(arr):
    def sort(start,end):
        if end - start == 0: # 배열의 길이가 1이하면 반환
            return
        mid = (start+end)//2 # 피벗을 다양하게 정할 수 있는 퀵정렬과 다르게 항상 절반으로 나누므로 고정
        
        sort(start, mid) # 앞쪽 절반 다시 sort
        sort(mid+1, end) # 뒷쪽 절반 다시 sort
        merge(start,mid,end) # 병합
    
    def merge(start,mid,end): # 이미 정렬된 두 배열을 하나로 합치면서 정렬하는 메서드
        global count
        global K
        global V
        
        temp = [] # 임시로 배열을 저장하는 리스트
        l, h = start, mid+1 # 앞뒤 배열의 각각의 비교 시작점(이미 정렬된 배열이므로 가장 앞 요소가 최솟값)
        
        while l <= mid and h <= end: # 비교 요소들이 모두 각각의 앞뒤 배열 안에 있을 때(어느 하나가 다 temp에 들어가기전에)
            if arr[l] <= arr[h]:  # 요소 중 작은 요소를        
                temp.append(arr[l]) # temp(병합배열)에 저장
                count += 1
                if count == K:
                    V = arr[l]
                l += 1 # 작은 요소가 temp에 들어갔으니 다음 요소와 비교를 위해 index값을 +1 해준다
            else: # arr[h]가 더 작은 경우
                temp.append(arr[h])
                count += 1
                if count == K:
                    V = arr[h]
                h += 1
                
        while l <= mid: # 왼쪽 배열 부분이 남은 경우
            temp.append(arr[l]) # 앞 배열에 남은 요소들을 temp에 전부 추가해준다
            count += 1
            if count == K:
                V = arr[l]
            l += 1
        while h <= end: # 오른쪽 배열 부분이 남은 경우
            temp.append(arr[h])
            count += 1
            if count == K:
                V = arr[h]
            h += 1
        
            
        for i in range(start,end+1):
            arr[i] = temp[i-start] # temp의 요소를 원래 배열에 넣어줘야하는데 temp[0]이 arr[0]은 꼭 아니므로 temp[i-start]를 해준다
    
           
    return sort(0,len(arr)-1) # 결국 실행하는 것은 sort 함수

N, K = map(int,sys.stdin.readline().strip().split())

inputList = list(map(int,sys.stdin.readline().strip().split()))

count = 0
value = 0

merge_sort(inputList)

try:
    print(V)
except NameError:
    print(-1)