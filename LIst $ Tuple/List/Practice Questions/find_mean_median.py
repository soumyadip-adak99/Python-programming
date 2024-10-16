arr = [1, 3, 4, 7, 9, 11]
sum = 0

for i in range(len(arr)):
    sum += arr[i]

mean = sum / len(arr)

if len(arr) % 2 == 0:
    median = (arr[len(arr) // 2 -1] + arr[len(arr) // 2]) / 2.0
else:
    median = arr[len(arr) // 2]

print("Mean:",mean)
print("Median:",median)