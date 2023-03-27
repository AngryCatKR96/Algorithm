def insertion_sort(list):
    prev = 0
    temp = 0
    for index in range(1,len(list)): # 첫 번째 요소는 제외하고 두 번째 요소부터 끝까지 index로 삼음
        temp = list[index] # temp는 index 위치의 값, 즉 비교할 기준이 되는 값
        prev = index-1 # prev는 index 바로 전의 값
        while prev >= 0 and temp < list[prev]: # prev 조건을 넣어주지 않으면 index가 두번째 요소에서 멈추지않음
            list[prev+1] = list[prev] # 기준 temp값이 비교할 값보다 작으면 prev에 있는 값을 뒤로 한칸 민다
            prev -= 1 # prev에서 1을 빼줌으로써 한칸 그 전에 비교한 위치보다 한칸 왼쪽에 있는 값과 비교하게 됨
        list[prev+1] = temp # while문을 탈출했을 때 prev 위치의 값은 temp보다 같거나(안정정렬이 되는 이유) 작은 값이된다
                            # 따라서 prev+1 위치는 빈 위치가 되므로 여기에 "삽입"해주면됨
    return list # 리스트 반환
    
N = list(map(int,input().split()))

print(insertion_sort(N))