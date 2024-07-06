#     1
#    212
#   32123
#  4321234

n = 5

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i, 0, -1):
        print(k, end="")
    for l in range(2, i + 1):
        print(l, end="")
    print()
