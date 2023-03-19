# Calculate the number of birthdays celebrated by Mr.X. If Mr.X was born on 29th February of a leap year then he
# celebrates birthday only in leap years. Given the date of birth of Mr.X and the current year, design an algorithm
# and write the Python code to determine the number of birthdays celebrated by Mr.X. A year is a leap year if it
# is divisible by 4 and not divisible by 100 or when the year is divisible by 400. For example, year 1996 and
# are leap years whereas 1900 is not a leap year. Assume that the current day and month is greater than day and month
# of birthday.


# so we just have to check number of leap year between user birthday year and current year


def calculate_total_leap_year():
    day_of_birt = int(input("please enter the day of birth: "))
    month_of_birth = int(input("please enter the month of birth: "))
    year_of_birth = int(input("please enter the year of birth: "))

    current_year = int(input("please enter the current year "))

    if current_year < year_of_birth:
        print(" ")
        print(" INVALID INPUT - Please enter the year greater than year of birth ")
        return 0

    elif month_of_birth == 2 and day_of_birt == 29:

        # checking if year of birth for nr x is leap of not
        is_leap_birth_year = year_of_birth % 4 == 0 and (year_of_birth % 100 != 0 or year_of_birth % 400 == 0)

        num_birthdays = 0
        for year in range(year_of_birth, current_year + 1):

            # checking if it is leap year or  and increment current year
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                num_birthdays += 1

        if is_leap_birth_year:
            num_birthdays = num_birthdays - 1

    else:
        num_birthdays = current_year - year_of_birth

    return num_birthdays


if __name__ == '__main__':
    num_birthdays = calculate_total_leap_year()
    print(" ")
    print("Mr.X has celebrated", num_birthdays, "birthdays so far.")
