def calcualte(x, n):
    if n == 0:
        return 1

    if n % 2 == 0:
        return calcualte(x, n // 2) ** 2
    else:
        return calcualte(x, n // 2) ** 2 * x


def main():
    x = 2
    n = 5
    ans = calcualte(x, n)
    print("Ans: ", ans)


if __name__ == "__main__":
    main()
