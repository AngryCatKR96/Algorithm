s = input()
start = 0
end = len(s)-1
result = 1

while start <= end:
    if s[start] == s[end]:
        start += 1
        end -= 1
    else:
        result = 0
        break
    
print(result)