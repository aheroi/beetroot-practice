import calendar
import datetime

print('Today is', datetime.datetime.now())

text_calendar = calendar.TextCalendar()
# text_calendar.prmonth(2022, 7)
year = int(input('Enter year: '))
text_calendar.pryear(year)
# text_calendar.prweek(13, 12)
