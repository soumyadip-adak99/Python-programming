# move first element at last of the index


def move_element(arr, temp):
    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]
    arr[len(arr) - 1] = temp


arr = [1, 2, 3, 4, 5]
temp = arr[0]
move_element(arr, temp)
print(arr)
