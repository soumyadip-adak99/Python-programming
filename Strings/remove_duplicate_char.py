def using_loop(str, new_str):
    for i in range(len(str)):
        if i == 0 or str[i] != str[i - 1]:
            new_str += str[i]
    print(new_str)

def using_set(str, new_str):
    n = set()

    for i in range(len(str)):
        char = str[i]
        if char not in n:
            new_str += str[i]
            n.add(char)
    print(new_str)

if __name__ == "__main__":
    str = "hello"
    new_str = " "

    using_loop(str, new_str) #using loop
    using_set(str, new_str) #using set