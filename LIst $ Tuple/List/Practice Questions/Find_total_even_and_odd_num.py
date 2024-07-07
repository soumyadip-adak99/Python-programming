# find total even or odd numbers in a array/list


def find_even_and_odd_num(arr):
    even = 0
    odd = 0

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even += 1
        else:
            odd += 1

    print("Total numbers of even numbers is: {}".format(even))
    print("Total numbers of odd numbers is: {}".format(odd))


arr = [1, 2, 3, 4, 5]
find_even_and_odd_num(arr)
