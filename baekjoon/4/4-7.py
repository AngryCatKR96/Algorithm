N = int(input())
seq = list(map(int,input().split()))

M = max(seq)

sum = 0

for i in range(N):
    seq[i] = seq[i]/M*100
    sum += seq[i]
    
avg = sum / N

print(avg)