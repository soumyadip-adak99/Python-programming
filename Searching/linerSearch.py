def liner_search(arr):
    print("List elements: ", arr)
    x = int(input("Enter your searching element: "))

    for i in range(len(arr)):
        if x == arr[i]:
            print(f"{x} find at index number: {i}")


if __name__ == "__main__":
    arr = [5, 1, 2, 3, 6, 7]
    liner_search(arr)
