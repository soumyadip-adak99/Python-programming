def copy_arr_elements(a, b):
    print("Original array:",a) #print original arrya

    #copy arr
    for i in range(len(a)):
        for j in range(len(a[i])):
            b[i][j] = a[i][j]

    print("Copy array:",b) #print copy array

if __name__ == "__main__":
    a = [
        [1, 2, 3, 4],
        [4, 5, 6, 7],
        [8, 9, 0, 1]
    ]
    b = [[0 for _ in range(len(a[0]))] for _ in range(len(a))]

    copy_arr_elements(a, b)