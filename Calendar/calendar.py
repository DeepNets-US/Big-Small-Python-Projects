import datetime

# Constants
MONTH_NAMES = (
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
)
WEEK_DAY_ABBREV = ("SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT")
DAYS_IN_WEEK = 7

# User Interface Display Constants
WEEK_DAY_ROW = "".join([f"     {day}   " for day in WEEK_DAY_ABBREV])
TOP_BORDER = "+----------"*DAYS_IN_WEEK + "+"
CELL_FORMAT = "|   {day:2}     "


def show_calendar(year, month):
    # Initializing the current date to the first day of the given year and month
    current_date = datetime.date(year, month, 1)

    # Finding the starting day of the month
    while current_date.weekday() != 6:
        current_date -= datetime.timedelta(days=1)

    # Display the days of the week
    print(WEEK_DAY_ROW)
    print(TOP_BORDER)

    while True:
        for _ in range(2):
            for i in range(DAYS_IN_WEEK):
                print(CELL_FORMAT.format(day=" "), end="")
                if i == DAYS_IN_WEEK - 1:
                    print("|", end="")
            print()

        for i in range(DAYS_IN_WEEK):
            print(CELL_FORMAT.format(day=current_date.day), end="")
            if i == DAYS_IN_WEEK - 1:
                print("|", end="")
            current_date += datetime.timedelta(days=1)
        print()

        for _ in range(2):
            for i in range(DAYS_IN_WEEK):
                print(CELL_FORMAT.format(day=" "), end="")
                if i == DAYS_IN_WEEK - 1:
                    print("|", end="")
            print()

        print(TOP_BORDER)

        if current_date.month != month:
            break


def get_valid_input(prompt, condition_check):
    while True:
        user_input = input(prompt + '\n>')
        if condition_check(user_input):
            return user_input
        print("Please enter a valid input.")


def is_valid_year(year):
    return year.isdecimal() and int(year) > 0


def get_year():
    return get_valid_input("Enter the Year", is_valid_year)


def is_valid_month(month):
    return month.isdecimal() and 1 <= int(month) <= 12


def get_month():
    return get_valid_input("Enter the Month (1-12)", is_valid_month)


def main():
    # User inputs for year and month
    year = int(get_year())
    month = int(get_month())

    # Output the calendar for the given year and month
    print(f"\t\t\t\t{MONTH_NAMES[month-1]} {year}\n")
    show_calendar(year, month)


if __name__ == "__main__":
    print("Calendar Maker by Utkarsh Saxena")
    main()
