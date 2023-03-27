seq = []

for i in range(9):
    seq.append(int(input()))
    
MaxNum = max(seq)
where = seq.index(MaxNum) + 1

print(MaxNum)
print(where)
