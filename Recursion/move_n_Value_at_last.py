def move_all_x_to_end(string, index, count, new_string):
    if index == len(string):
        new_string += 'x' * count
        print(new_string)
        return

    if string[index] == 'x':
        count += 1
        move_all_x_to_end(string, index + 1, count, new_string)
    else:
        new_string += string[index]
        move_all_x_to_end(string, index + 1, count, new_string)


if __name__ == "__main__":
    string = "aabbxccxddxgxg"
    move_all_x_to_end(string, 0, 0, "")
