#! python3
# findDate.py - Cleaning up dates in different date formats (such as 3/14/2019, 03-14-2019, and
# 2015/3/19) by replacing them with dates in a single, standard format.
import pyperclip
import re

# Define the regex pattern
dateRegex = re.compile(
    r'\b(?P<month>\d{1,2})[/-](?P<day>\d{1,2})[/-](?P<year>(\d{2}|\d{4}))\b|'
    r'\b(?P<year2>\d{4})[/-](?P<month2>\d{1,2})[/-](?P<day2>\d{1,2})\b'
)

# Function to standardize date format
def standardize_dates(text):
    def replace_date(match):
        # Check which pattern matched and extract values
        if match.group('month'):  # First pattern matched
            month = int(match.group('month'))
            day = int(match.group('day'))
            year = match.group('year')
            if len(year) == 2:  # Convert 2-digit year to 4-digit
                year = '20' + year  # Adjust as needed (e.g., '20' for 2000s)
            return f"{year}-{month:02d}-{day:02d}"  # Format to YYYY-MM-DD
        else:  # Second pattern matched
            year = match.group('year2')
            month = int(match.group('month2'))
            day = int(match.group('day2'))
            return f"{year}-{month:02d}-{day:02d}"  # Format to YYYY-MM-DD

    # Substitute dates with standardized format
    return re.sub(dateRegex, replace_date, text)

# Example usage
text = pyperclip.paste()
cleaned_text = standardize_dates(text)
print(cleaned_text)

