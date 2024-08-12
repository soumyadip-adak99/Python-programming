def concqure(arr, str_idx, mid, end_idx):
    newArr = []

    idx_1 = str_idx
    idx_2 = mid + 1

    while (idx_1 <= mid and idx_2 <= end_idx):
        if arr[idx_1] < arr[idx_2]:
            newArr.append(arr[idx_1])
            idx_1 += 1
        else:
            newArr.append(arr[idx_2])
            idx_2 += 1

    while (idx_1 <= mid):
        newArr.append(arr[idx_1])
        idx_1 += 1

    while (idx_2 <= end_idx):
        newArr.append(arr[idx_2])
        idx_2 += 1

    for i in range(len(newArr)):
        arr[str_idx + i] = newArr[i]


def divide(arr, str_idx, end_idx):
    if str_idx >= end_idx:
        return

    mid = str_idx + (end_idx - str_idx) // 2

    divide(arr, str_idx, mid)
    divide(arr, mid + 1, end_idx)
    concqure(arr, str_idx, mid, end_idx)


if __name__ == "__main__":
    arr = [4, 6, 5, 1, 2, 3]
    size = len(arr)
    divide(arr, 0, size - 1)
    print(arr)
