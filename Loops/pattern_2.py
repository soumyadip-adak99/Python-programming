# *****
# *   *
# *   *
# *****

n = 5
m = 5

i = 1
while i <= n:
    j = 1
    while j <= m:
        if (i == 1 or j == 1) or (i == n or j == m):
            print("*", end="")
        else:
            print(" ", end="")
        j += 1
    print()
    i += 1
