def find_occurrences(str, index, element, first_index, last_index):
    # base case
    if index == len(str):
        print(first_index, last_index)
        return

    if str[index] == element:
        if first_index == -1:
            first_index = index
        last_index = index

    find_occurrences(str, index + 1, element, first_index, last_index)


if __name__ == "__main__":
    str = "abaaahhba"
    element = 'a'
    first_index = -1
    last_index = -1
    find_occurrences(str, 0, element, first_index, last_index)
