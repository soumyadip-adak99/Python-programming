def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    ch = list(s)
    i = 0
    j = len(ch) - 1

    while i < j:
        while i < j and ch[i] not in vowels:
            i += 1
        while i < j and ch[j] not in vowels:
            j -= 1
        if i < j:
            ch[i], ch[j] = ch[j], ch[i]
            i += 1
            j -= 1

    return ''.join(ch)

if __name__ == "__main__":
    print(reverse_vowels("hello"))
