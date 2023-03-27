def d(n):
    m = str(n)
    result = n
    for i in range(len(m)):
        result += int(m[i])
    return result

numbers = [num for num in range(1,10001)]

for i in range(1,10001):
    try:
        result = d(i)
        numbers.remove(result)
    except:
        pass
    
for i in range(len(numbers)):
    print(numbers[i])