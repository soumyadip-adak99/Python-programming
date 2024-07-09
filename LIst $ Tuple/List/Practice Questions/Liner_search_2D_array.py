# Liner search in 2D array


def liner_search(arr, x):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == x:
                print(x, "found at row of", i + 1, "and columns of", j + 1)


arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x = 5
liner_search(arr, x)
