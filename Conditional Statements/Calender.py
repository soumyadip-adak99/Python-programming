def week_chart(remainder: int) -> str:
    week_days = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday"
    }
    return week_days.get(remainder, "Invalid day")


def month_chart(month: int) -> int:
    if 1 <= month <= 12:
        if month in [1, 10]:
            return 0
        elif month in [2, 3, 11]:
            return 3
        elif month in [4, 7]:
            return 6
        elif month == 5:
            return 1
        elif month == 6:
            return 4
        elif month == 8:
            return 2
        else:
            return 5
    return 0


def century_chart(year: int) -> int:
    century = year // 100
    remainder = century % 4

    century_code = {
        0: 6,
        1: 4,
        2: 2,
        3: 0
    }
    return century_code.get(remainder, 0)


def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def get_week_day(day: int, month: int, year: int):
    last_two_digits = year % 100
    cosent = last_two_digits // 4

    if is_leap_year(year):
        result = (day + month_chart(month) + century_chart(year) + last_two_digits + cosent - 1) % 7
        print(f"{week_chart(result)}")

    else:
        result = (day + month_chart(month) + century_chart(year) + last_two_digits + cosent) % 7
        print(f"{week_chart(result)}")


if __name__ == "__main__":
    get_week_day(day=11, month=8, year=2031)
