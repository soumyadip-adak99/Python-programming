def copy_arr_elements(a, b):
    print("A:",a)
    
    for i in range(len(a)):
        for j in range(len(a[i])):
            b[i][j] = a[i][j]
    
    print("B:",b)

if __name__ == "__main__":
    a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    b = [[0 for _ in range(len(a[0]))] for _ in range(len(a))]
    
    copy_arr_elements(a, b)