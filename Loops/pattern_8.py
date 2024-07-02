# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

n = 5
number = 1

for i in range(n + 1):
    for j in range(i + 1):
        print(number, end=" ")
        number += 1
    print()
