a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
b = [[0 for _ in range(len(a))] for _ in range(len(a))]

#copy 2D array elements
for i in range(len(a)):
    for j in range(len(a)):
        b[i][j] = a[i][j]

# print array of A
print("Array of A:")
for i in range(len(a)):
    for j in range(len(a)):
        print(f"{a[i][j]}",end="")
    print()

#print array of b
print("Array of A:")
for i in range(len(a)):
    for j in range(len(a)):
        print(f"{b[i][j]}", end="")
    print()
