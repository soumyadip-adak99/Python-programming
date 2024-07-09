# find both the 2d array  is equl or not


def find_2D_array_equal_or_not(array_a, array_b):
    if len(array_a) != len(array_b):
        return False
    else:
        for i in range(len(array_a)):
            for j in range(len(array_a)):
                if array_a[i][j] != array_b[i][j]:
                    return False
    return True


array_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
array_b = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
array_equals = find_2D_array_equal_or_not(array_a, array_b)

if array_equals:
    print("Both the array eleemtn is euql")
else:
    print("NOT EQUAL")
