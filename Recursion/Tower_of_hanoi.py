def tower_of_hanoi(n, scorce, helper, destination):
    if n == 1:
        print(f"stack {n} move {scorce} to {destination}")
        return

    # if n - 1 = 2 then stack move scorce
    tower_of_hanoi(n - 1, scorce, destination, helper)  # first step count from n -1
    print(f"stack {n} move {scorce} to {destination}")
    tower_of_hanoi(n - 1, helper, scorce, destination)  # second part count from n - 1


def main():
    n = 3
    scorce = "scorce"
    helper = "hlper"
    destination = "destination"
    tower_of_hanoi(n, scorce, helper, destination)


if __name__ == "__main__":
    main()
