def bianry_search(arr, target):
    arr.sort()
    start_idx = 0
    end_idx = len(arr)

    while (start_idx <= end_idx):
        mid = start_idx + (end_idx - start_idx) // 2
        if target < arr[mid]:
            end_idx = mid + 1
        elif target > arr[mid]:
            start_idx = mid - 1
        else:
            return mid

        return -1


if __name__ == "__main__":
    arr = [5, 3, 1, 2, 4]
    target = 3
    ans = bianry_search(arr, target)

    if ans != -1:
        print(f"The target element {target} find at index : {ans}")
    else:
        print("NOT FOUND !")
