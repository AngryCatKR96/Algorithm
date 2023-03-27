N = int(input())

count = 1
x = 1
y = 1

while count < N:
    if x == 1 and y % 2 == 1:
        y = y+1
        count += 1
        while count < N and y > 1:
            y -= 1
            x += 1
            count += 1
    elif x % 2 == 0 and y == 1:
        x = x+1
        count += 1
        while count < N and x > 1:
            x -= 1
            y += 1
            count += 1
            
    
print(str(x)+"/"+str(y))