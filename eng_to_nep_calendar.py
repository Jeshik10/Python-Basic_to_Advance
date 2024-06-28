# Create Software that convert English Date to Nepali Date

import datetime
import datetime_nepali

year =  int(input("Enter the year: "))
month =  int(input("Enter the month: "))
day =  int(input("Enter the day: "))

date = datetime_nepali.date.from_datetime_date(datetime.date(year, month, day))
print(f"Nepali Date: {date}")