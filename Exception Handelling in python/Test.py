def divide(a, b):
    try:
        return a // b
    except Exception as e:
        return -1


if __name__ == "__main__":
    numerator = [10, 200, 30, 40]
    denominatros = [1, 2, 0, 4]

    for i in range(5):
        try:
            print(divide(numerator[i], denominatros[i]))
        except Exception as e:
            print(e)

    print('Good job :)')
