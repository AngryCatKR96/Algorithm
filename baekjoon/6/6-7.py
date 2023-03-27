A, B = input().split()

reverse_A = ""
reverse_B = ""


for x in A:
    reverse_A = x + reverse_A
    
for x in B:
    reverse_B = x + reverse_B
    
reverse_A = int(reverse_A)
reverse_B = int(reverse_B)

if reverse_A > reverse_B:
    print(reverse_A)
else:
    print(reverse_B)
