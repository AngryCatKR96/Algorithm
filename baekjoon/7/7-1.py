A, B, C = map(int,input().split())

N = 0

#result = int(A/(C-B)) + 1 # 여기  result넣으면 ZeroDivisionError가 발생한다.

if (C-B) <= 0:
    print(-1)
else:
    result = int(A/(C-B)) + 1 # result를 if앞이 아닌 else:안에 넣어줌으로써 (C-B)가 0이 될때 나눗셈을 안함
    print(result)
