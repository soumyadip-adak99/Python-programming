# find second largest value in array/list


def find_secon_largest_value(arr):

    arr.sort()  # sort the array
    num = 0

    for i in range(len(arr) - 1):
        num = arr[i]

    print("The second largest value in the array/list is:", num)


arr = [2, 1, 3, 4]
find_secon_largest_value(arr)
