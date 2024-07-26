def tower_of_hanoi(n, scroce, helper, destination):
    if n == 1:
        print(f"{n} move from {scroce} to {destination}")
        return

    # n-1 -> scorce = scorce , helper = destination, destination = helper
    tower_of_hanoi(n - 1, scroce, destination, helper)  # first part
    # print statement
    print(f"{n} move from {scroce} to {destination}")
    # n == n -> scorce = helper, helper = scorce, destionation = destionaton
    tower_of_hanoi(n - 1, helper, scroce, destination)  # second part


def main():
    n = 3
    scroce = "scroce"
    helper = "helper"
    destination = "destination"
    tower_of_hanoi(n, scroce, helper, destination)


if __name__ == "__main__":
    main()
