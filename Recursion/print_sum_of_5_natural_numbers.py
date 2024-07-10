# Print sum of first 5 natural number


def sum_calculate(i, n, sum):
    if i == n:
        sum += i
        print(sum)
        return

    sum += i
    sum_calculate(i + 1, n, sum)


sum_calculate(0, 5, 0)
