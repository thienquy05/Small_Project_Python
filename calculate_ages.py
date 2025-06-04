import datetime

current_year = datetime.date.today().year
current_month = datetime.date.today().month
current_day = datetime.date.today().day

print("Please enter your birth day")
birth_year = int(input("Year of birth: "))
birth_month = int(input("Month of birth: "))
birth_day = int(input("Day of birth: "))

age_year = current_year - birth_year
age_month = abs(current_month - birth_month)
age_day = abs(current_day - birth_day)

print("Your current age is:", age_year, "age", age_month, "month", "and", age_day, "day")
