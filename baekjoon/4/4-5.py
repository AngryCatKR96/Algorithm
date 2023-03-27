seq = []
result = []


for i in range(28):
    seq.append(int(input()))
    
for i in range(30):
    try:
        where = seq.index(i+1)
    except:
        result.append(i+1)
        
if result[0] < result[1]:
    print(result[0])
    print(result[1])
else:
    print(result[1])
    print(result[0])
    