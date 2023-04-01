""" 스택을 이용해야함. (면 스택에 넣고 )면 스택에서 하나 뺌
뺄 (가 없거나 다 끝났는데도 스택에 (가 남아있으면 NO"""
import sys

T = int(input())

for _ in range(T):
    PS = sys.stdin.readline().strip()
    VPS = True
    stack = []
    
    for i in range(len(PS)):
        try:
            if PS[i] == '(':
                stack.append('(')
            else:
                stack.pop()
        except:
            print('NO')
            VPS = False
            break
        
    if VPS == True:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')
    

    
        