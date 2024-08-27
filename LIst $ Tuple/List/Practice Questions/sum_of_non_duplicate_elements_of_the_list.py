def sum_of_non_duplicate_elements(arr):
    arr.sort()  # sort the array

    idx = 0
    size = 0
    sum = 0
    newArr = []

    for i in range(len(arr) - 1):
        if (arr[i] != arr[i + 1]):
            arr[idx] = arr[i]
            newArr.append(arr[idx])
            idx += 1
            size += 1

    print(f"Non duplicate element: {newArr}")
    for i in range(size):
        sum += arr[i]

    print(f"Sum: {sum}")


if __name__ == "__main__":
    arr = [10, 20, 10, 30]
    sum_of_non_duplicate_elements(arr)
