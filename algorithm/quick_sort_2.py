def quick_sort(arr):
    def out_sort(start,end):
        if start >= end: # 부분 배열이 최소 크기(1)이 되면 끝
            return
        
        mid = in_sort(start,end) #2 1차 정렬이 끝난 뒤 기준점을 mid로 선언
        out_sort(start,mid-1) # 재귀함수로 #2 과정을 앞쪽 부분수열에서 다시 함
        out_sort(mid,end) # 재귀함수로 #2 과정을 뒷쪽 부분수열에서 다시 함
        
    def in_sort(start,end):
        pivot = arr[(start+end)//2] # 피벗은 가운데 값으로 한다
        while start <= end: # start와 end가 각각 가운데를 향해 가면서 엇갈릴 때 까지 실행
                            #(엇갈렸다면 피벗을 기준으로 좌우를 다 확인했다는 말이니 더 확인할 필요가 없다)
            while arr[start] < pivot: # 배열의 값을 앞에서부터 찾아서 피벗보다 크거나 같은 값의 위치를 찾자
                start += 1
            while arr[end] > pivot: # 배열의 값을 뒤에서부터 찾아서 피벗보다 작거나 같은 값의 위치를 찾자
                end -= 1
            if start <= end: # 위치를 찾았는데 둘의 위치가 엇갈리지 않았더라면
                arr[start], arr[end] = arr[end], arr[start] # 둘의 위치를 교환하고
                start, end = start +1, end -1 # 각각의 진행방향대로 한칸씩 이동
                
        return start # 1차적으로 정렬이 끝났으면 부분 배열을 나누는 기준점을 반환
        
    return out_sort(0,len(arr)-1)

arr = list(map(int,input().split()))

quick_sort(arr)

print(arr)