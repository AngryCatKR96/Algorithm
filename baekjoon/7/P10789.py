result = []
for _ in range(5):
    str = input()
    result.append(list(str))

for i in range(15):
    for j in range(5):
        try:
            print(result[j][i], end="")
        except IndexError:
            continue