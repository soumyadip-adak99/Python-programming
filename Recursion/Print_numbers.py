# print 5 to 1 nubers using recursion
def print_number(n):
    if n == 0:
        return

    print(n)
    print_number(n - 1)


n = 5
print_number(n)
