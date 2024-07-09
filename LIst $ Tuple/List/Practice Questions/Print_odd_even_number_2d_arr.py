def find_odd_even_numbers(arr):
    total_odd_num = 0
    total_even_num = 0

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] % 2 == 0:
                total_even_num += 1
            else:
                total_odd_num += 1

    print(f"Total even numbers: {total_even_num}")
    print(f"Total odd numbers: {total_odd_num}")


arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
find_odd_even_numbers(arr)
