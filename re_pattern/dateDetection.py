#! python3
#  Writes a regular expression that can detect dates in the DD/MM/YYYY format.
# Assume that the days range from 01 to 31, the month range from 01 to 12,
# and the year range from 1000 to 2999. Note that if the day or month is a single digit,
# it’ll have a leading zero.
# The regular expression doesn’t have to detect correct days for each month or for leap years;
# it will accept nonexistent dates like 31/02/2020 or 31/04/2021.
# Then store these strings into variables named month, day, and year,
# and write additional code that can detect if it is a valid date.
#   April, June, September, and November have 30 days,
#   February has 28 days, and the rest of the months have 31 days.
#   February has 29 days in leap years.
# Leap years are every year evenly divisible by 4, except for years evenly divisible by 100,
# unless the year is also evenly divisible by 400.
# Note how this calculation makes it impossible to make a reasonably sized regular expression
#   that can detect a valid date.

import re
import pyperclip

def is_valid_date(day, month, year):
    is_leap = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
    # Determine the maximum days in the month
    if month in {1,3,5,78,10,12}:
        max_days = 31
    elif month in {4,6,9,11}:
        max_days = 30
    elif month == 2:
        max_days = 29 if is_leap else 28
    else:
        return False
    return day <= max_days

dateRegex = re.compile(r'(?P<day>0[1-9]|[12][0-9]|30|31)'
                       r'\/'
                       r'(?P<month>0[1-9]|1[0-2])'
                       r'\/'
                       r'(?P<year>1000|1[0-9]{3}|20[0-2][0-9]|2[01][0-9]{2}|2999)')

text = pyperclip.paste()
matches = dateRegex.finditer(text)
for match in matches:
    if match:
        day = int(match.group('day'))
        month = int(match.group('month'))
        year = int(match.group('year'))
        print(f"Day: {day}, Month: {month}, Year: {year}")

        if is_valid_date(day, month, year):
            print("The date is valid.")
        else:
            print("The date is invalid.")
