def quick_sort(list):
    if len(list) <= 1:
        return list
    
    pivot = list[len(list)//2] # 피벗은 정가운데 있는 값으로 설정
    
    less_list, eq_list, more_list = [], [], [] # 피벗보다 크고 작은 요소들 넣을 리스트 생성
    
    for i in range(len(list)): # 반복문을 통해 정렬해준다
        if list[i] < pivot:
            less_list.append(list[i])
        elif list[i] > pivot:
            more_list.append(list[i])
        else:
            eq_list.append(list[i])
            
    return quick_sort(less_list) + eq_list + quick_sort(more_list) # 반환은 정렬해서 합친 리스트

list = list(map(int,input().split()))

print(quick_sort(list))
