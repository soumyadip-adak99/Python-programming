arr = [1, 2, 3, 4]
print("Initial array:", arr)
n = int(input("Enter element to delete from the array: "))

for i in range(len(arr)):
    if arr[i] == n:
        for j in range(i, len(arr) - 1):
            arr[j] = arr[j + 1]
        arr.pop()
        break


print("Array after deletion:", arr)
