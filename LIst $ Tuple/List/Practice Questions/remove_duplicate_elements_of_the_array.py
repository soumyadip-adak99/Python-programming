#using 2 array  -> method 1
def remove_duplicate(duplicate_array_elements, non_duplicate_array_elements):
    print("Original Array:",duplicate_array_elements)
    #sort this array
    duplicate_array_elements.sort()

    #remove duplicate elements
    for i in range(len(duplicate_array_elements) - 1):
        if duplicate_array_elements[i] != duplicate_array_elements[i + 1]:
            non_duplicate_array_elements.append(duplicate_array_elements[i])

    print("After removing duplicate elements:",non_duplicate_array_elements)

if __name__ == "__main__":
    duplicate_array_elements = [10, 20, 10, 30, 40, 20, 10, 40, 50]
    non_duplicate_array_elements = []

    remove_duplicate(duplicate_array_elements, non_duplicate_array_elements)



#method -> 2
def remove_duplicate(duplicate_array_elements):
    print("Original Array:",duplicate_array_elements)
    #sort this array
    duplicate_array_elements.sort()

    #remove duplicate elements
    j = 0
    size_of_new_arr = 0
    for i in range(len(duplicate_array_elements) - 1):
        if duplicate_array_elements[i] != duplicate_array_elements[i + 1]:
            duplicate_array_elements[j] = duplicate_array_elements[i]
            j += 1
            size_of_new_arr += 1

    print("After removing duplicate elements:", end=" ")
    for i in range(size_of_new_arr):
        print(duplicate_array_elements[i], end=" ")


if __name__ == "__main__":
    duplicate_array_elements = [10, 20, 10, 30, 40, 20, 10, 40, 50]

    remove_duplicate(duplicate_array_elements)










































