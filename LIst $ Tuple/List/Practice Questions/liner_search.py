# liner search in list


def liner_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            print(x, "find ar index number: ", i)
            break
        else:
            print("NOT FOUND")


arr = [1, 2, 3]
x = 1
liner_search(arr, x)
