# find both the array/list elements equal or not


def find_array_equlas(arr_a, arr_b, array_equals):
    if len(arr_a) != len(arr_b):
        array_equals = False
    else:
        for i in range(len(arr_a)):
            if arr_a[i] != arr_b[i]:
                array_equals = False
                break

    if array_equals:
        print("Both the array/list are equal.")
    else:
        print("Both the array/list are not equal")


arr_a = [1, 2, 3]
arr_b = [1, 2, 3]
array_equals = True
find_array_equlas(arr_a, arr_b, array_equals)
