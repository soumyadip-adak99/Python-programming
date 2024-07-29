def concqure(left, right):
    merged_array = []

    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_array.append(left[i])
            i += 1
        else:
            merged_array.append(right[j])
            j += 1

    while i < len(left):
        merged_array.append(left[i])
        i += 1

    while j < len(right):
        merged_array.append(right[j])
        j += 1

    return merged_array


def divide(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2

    left = divide(arr[:mid])
    right = divide(arr[mid:])

    return concqure(left, right)


if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    result = divide(arr)
    print(result)
