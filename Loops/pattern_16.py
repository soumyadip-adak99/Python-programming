#    *
#   ***
#  *****
# *******
# *******
#  *****
#   ***
#    *

num = 5
# upper part
for i in range(1, num + 1):
    for j in range(num - i):
        print(" ", end="")
    for k in range(1, i + 1):
        print("* ", end="")
    print()
# lower part
for i in range(num, 0, -1):
    for j in range(num - i):
        print(" ", end="")
    for k in range(1, i + 1):
        print("* ", end="")
    print()
