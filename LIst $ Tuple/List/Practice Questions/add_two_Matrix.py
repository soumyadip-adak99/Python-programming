def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()


def add_tow_matrix(a, b):
    row = len(a)
    col = len(b)
    c = [[0 for _ in range(len(a[0]))] for _ in range(len(a))]
    for i in range(row):
        for j in range(col):
            c[i][j] = a[i][j] + b[i][j]
    return c


def main():
    a = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
    print("Matrix A: ")
    print_matrix(a)

    b = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
    print("\nMatrix B: ")
    print_matrix(b)

    c = add_tow_matrix(a, b)
    print("\nResult")
    print_matrix(c)


if __name__ == "__main__":
    main()
