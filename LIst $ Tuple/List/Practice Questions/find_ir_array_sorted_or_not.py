def calcualte_array(arr, is_sorted):
    for i in range(len(arr)):
        for j in range(i + 1, (len(arr))):
            if arr[i] > arr[j]:
                is_sorted = False
                break

    if is_sorted:
        print("The array is sorted.")
    else:
        print("The array is not sorted.")


def main():
    arr = [1, 2, 3, 4]
    is_sorted = True
    calcualte_array(arr, is_sorted)


if __name__ == "__main__":
    main()
