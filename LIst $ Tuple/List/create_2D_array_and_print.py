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





