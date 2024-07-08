# move all the zeros at last of the index


def move_all_zeros(arr):
    n = 0
    size = len(arr)

    for i in range(size):
        if arr[i] != 0:
            temp = arr[n]
            arr[n] = arr[i]
            arr[i] = temp
            n += 1


arr = [0, 1, 0, 2, 0, 3]
move_all_zeros(arr)
print(arr)
