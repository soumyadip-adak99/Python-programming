def print_original_array(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=" ")
        print()


def modify_array(transpose, arr):
    for i in range(len(transpose)):
        for j in range(len(transpose[i])):
            transpose[i][j] = arr[j][i]

    return transpose


def main():
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Original array: ")
    print_original_array(arr)

    transpose = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
    modify_array(transpose, arr)

    print("\nModify array: ")
    for i in range(len(transpose)):
        for j in range(len(transpose[i])):
            print(transpose[i][j], end=" ")
        print()


if __name__ == "__main__":
    main()
