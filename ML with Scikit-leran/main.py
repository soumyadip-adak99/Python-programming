def find_min(data):
    total = 0
    for num in data:
        total += num

    return total // len(data)


def find_mode(data):
    mode = {}
    result = []

    for i in data:
        if i in mode:
            mode[i] += 1
        else:
            mode[i] = 1

    for num in mode:
        if mode[num] > 1:
            result.append(num)

    return result


def find_meadian(data):
    if len(data) < 0:
        return None

    data = sorted(data)
    n = len(data)
    middle = n // 2

    return data[middle] if n % 2 == 1 else (data[middle - 1] + data[middle]) / 2


if __name__ == "__main__":
    data = [50, 70, 70, 45, 76, 99, 88]
    mean = find_min(data)
    meadian = find_meadian(data)
    mode = find_mode(data)

    print(f"Mean: {mean}\nMeadian: {meadian}\nMode: {mode}")
