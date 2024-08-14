if __name__ == "__main__":
    n = int(input("Enter any number: "))

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                print("&", end=" ")
            elif i == 1 or i == n or j == 1 or j == n:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
