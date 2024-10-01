# print 2d array
row = int(input("Enter the size of the row: "))
col = int(input("Enter the size of the column: "))

arr = []
# enter array elements
for i in range(row):
    row = []
    for j in range(col):
        row.append(int(input(f"Enter element for row {i+1}, columns{j+1} : ")))
    arr.append(row)

# print the array elements
for i in range(len(arr)):
    for j in range(len(arr)):
        print(arr[i][j], end="")
    print()




# diffrent way

row = 3
col = 3

#create a 2 d array
arr = [[0 for _ in range(row)] for _ in range(col)]

#add elements in array
for i in range(row):
    for j in range(col):
        arr[i][j] = input(f"input {i} {j}: ")

for i in range(row):
    for j in range(col):
        print(f"| {arr[i][j]} |", end="")
    print()
