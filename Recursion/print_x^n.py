def calcualte(x, n):
    if n == 0:
        return 1

    xPower = calcualte(x, n - 1)
    calPower = x * xPower
    return calPower


def main():
    x = 2
    n = 5
    ans = calcualte(x, n)
    print("Ans: ", ans)


if __name__ == "__main__":
    main()
