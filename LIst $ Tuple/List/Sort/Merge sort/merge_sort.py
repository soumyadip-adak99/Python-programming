def conquer(arr, s_index, mid, e_index):
    merged_arr = [0] * (e_index - s_index + 1)
    index1 = s_index
    index2 = mid + 1
    x = 0

    while index1 <= mid and index2 <= e_index:
        if arr[index1] <= arr[index2]:
            merged_arr[x] = arr[index1]
            index1 += 1
        else:
            merged_arr[x] = arr[index2]
            index2 += 1
        x += 1

    while index1 <= mid:
        merged_arr[x] = arr[index1]
        index1 += 1
        x += 1

    while index2 <= e_index:
        merged_arr[x] = arr[index2]
        index2 += 1
        x += 1

    for i in range(len(merged_arr)):
        arr[s_index + i] = merged_arr[i]


def divide(arr, s_index, e_index):
    if s_index >= e_index:
        return

    mid = s_index + (e_index - s_index) // 2
    divide(arr, s_index, mid)
    divide(arr, mid + 1, e_index)
    conquer(arr, s_index, mid, e_index)


def main():
    arr = [6, 3, 9, 5, 2, 8]
    size = len(arr)

    divide(arr, 0, size - 1)

    for i in range(len(arr)):
        print(arr[i], end=" ")


if __name__ == "__main__":
    main()
