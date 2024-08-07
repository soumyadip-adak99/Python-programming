def conqcure(left, right):
    new_arr = []

    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new_arr.append(left[i])
            i += 1
        else:
            new_arr.append(right[j])
            j += 1

    while (i < len(left)):
        new_arr.append(left[i])
        i += 1

    while (j < len(right)):
        new_arr.append(right[j])
        j += 1

    return new_arr


def divided(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2

    left = divided(arr[:mid])
    right = divided(arr[mid:])

    return conqcure(left, right)


if __name__ == "__main__":
    arr = [5, 3, 4, 1, 2]
    ans = divided(arr)
    print(ans)
