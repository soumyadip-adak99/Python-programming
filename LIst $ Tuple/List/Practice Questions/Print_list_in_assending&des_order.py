# print list in aseding and desending

# using sort method
# arr = [2, 3, 4, 1]
# arr.sort()
# print(arr)


def sort_array(arr, order="asending"):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if order == "asending" and arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            elif order == "desending" and arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    if order == "asending":
        print("Array sort in asending order: ", arr)
    else:
        print("Array sort in desending order: ", arr)


arr = list(map(int, input("Enter the array/list elements: ").split()))
sort_array(arr.copy())
sort_array(arr, order="desending")
