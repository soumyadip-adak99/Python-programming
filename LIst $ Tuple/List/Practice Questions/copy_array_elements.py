def copy_array_elemnt(a, b):
    for i in range(len(a)):
         b.append(a[i])

    print("Array of A elements:",a)
    print("Array of B elements:",b)

if __name__ == "__main__":
    a = [1, 2, 3]
    b = []
    copy_array_elemnt(a, b)