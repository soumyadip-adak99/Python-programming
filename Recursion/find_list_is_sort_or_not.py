def isSorted(arr, index):
    #base case
    if index == len(arr) - 1:
        return True

    if arr[index] >= arr[index + 1]:
        return False

    return isSorted(arr, index + 1)


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    index = 0
    print(isSorted(arr, index))
