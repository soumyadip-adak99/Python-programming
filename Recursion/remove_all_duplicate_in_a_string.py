def remove_duplicate_string(string, str_idx, new_str, map):
    if str_idx == len(string):
        print(new_str)
        return

    current_char = string[str_idx]

    if map[ord(current_char) - ord('a')]:
        remove_duplicate_string(string, str_idx + 1, new_str, map)
    else:
        new_str += current_char
        map[ord(current_char) - ord('a')] = True
        remove_duplicate_string(string, str_idx + 1, new_str, map)

if __name__ == "__main__":
    string = "aabbbcc"
    map = [False] * 26
    remove_duplicate_string(string, 0, "", map)