# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

n = 5

for i in range(1, n + 1):  # upper part
    for j in range(1, i + 1):
        print("*", end="")
    space = int(2 * (n - i))
    for k in range(1, space + 1):
        print(" ", end="")
    for l in range(1, i + 1):
        print("*", end="")
    print()
for m in range(n - 1, 0, -1):  # lower part
    for o in range(1, m + 1):
        print("*", end="")
    space = int(2 * (n - m))
    for p in range(1, space + 1):
        print(" ", end="")
    for q in range(1, m + 1):
        print("*", end="")
    print()
