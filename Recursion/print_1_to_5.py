def print_number(n):
    if n == 6:
        return

    print(n, end=" ")
    print_number(n + 1)


n = 1
print_number(n)
