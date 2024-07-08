# find the second largest value in the array


def find_second_lagest_value(arr):
    arr.sort(reverse=True)
    return arr[1]


arr = [1, 3, 6, 4, 2, 5]
second_largest_value = find_second_lagest_value(arr)
print(second_largest_value)
