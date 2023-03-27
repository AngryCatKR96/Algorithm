N = int(input())

num5 = N // 5
num3 = (N-5*num5) // 3
left = (N-5*num5) % 3

"""
if num5 == 0 and num3 == 0:
    result =-1
elif left == 0:
    result = num5 + num3
elif left == 1 and num5 != 0:
    result = num5 + num3 +1
elif num5 == 0 and left ==1:
    result = -1
elif left == 2 and num5 >= 2:
    result = num5 + num3 +2
elif left == 2 and num5 < 2:
    result = -1
"""

if num5 == 0 and num3 == 0:
    result =-1
    
elif left == 0:
    result = num5 + num3
elif left == 1:
    if num5 != 0:
        result = num5 + num3 +1
    else:
        result = -1
elif left == 2:
    if num5 >= 2:
        result = num5 + num3 +2
    else: 
        result = -1
        
print(result)

