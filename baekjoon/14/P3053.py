""" 택시 기하학에서 원의 넓이?? 중점을 (0,0)으로 단순화해서 생각해보면 D = |x| + |y| 즉 원점을 중심으로하는 마름모의 넓이가 된다."""
import math

# 반지름 입력
R = int(input())

# 유클리드 기하학
print(format(math.pi*R*R, '.6f'))

# 택시 기하학, 마름모 넓이
print(format(R*R*2,".6f"))

