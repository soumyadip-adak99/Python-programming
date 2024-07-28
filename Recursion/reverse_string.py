def reverse_string(str, str_index):
    if str_index == 0:
        print(str[str_index], end=" ")
        return

    print(str[str_index], end=" ")
    reverse_string(str, str_index - 1)


if __name__ == "__main__":
    str = "ABCD"
    reverse_string(str, len(str) - 1)
