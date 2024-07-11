def print_original_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()


def modify_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == 0 or j == 0 or i == len(matrix) - 1 or j == len(matrix) - 1:
                print(matrix[i][j], end=" ")
            else:
                print(" ", end=" ")
        print()


def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print("Original matrix: ")
    print_original_matrix(matrix)

    print("\nModify matrix: ")
    modify_matrix(matrix)


if __name__ == "__main__":
    main()
