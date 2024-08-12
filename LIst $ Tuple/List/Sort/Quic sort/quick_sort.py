def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            # swaping
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    i += 1
    temp = arr[i]
    arr[i] = pivot
    arr[high] = temp
    return i


def quick_sort(arr, low, high):
    if low < high:
        pivot_idx = partition(arr, low, high)

        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)


if __name__ == "__main__":
    arr = [6, 2, 1, 3, 5, 4]
    quick_sort(arr, 0, len(arr) - 1)
    print(*arr)
