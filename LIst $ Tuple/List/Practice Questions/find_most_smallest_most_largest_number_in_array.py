# find most smallest and most largest number in array


def find_number(arr):
    arr.sort()

    most_smallest_number = arr[0]
    most_largest_number = arr[len(arr) - 1]

    print(most_smallest_number, "is a most smallest number in the array")
    print(most_largest_number, "is a most largest number in the array")


arr = [1, 3, 2, 4, 6, 5]
find_number(arr)
