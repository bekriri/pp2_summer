# dates and time

from datetime import datetime, date, timedelta

# current date and time
now = datetime.now()
print("now:", now)

today = date.today()
print("today:", today)

# creating date objects
d = date(2005, 6, 15)
print("my date:", d)

# formatting dates
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%B %d, %Y"))
print(now.strftime("%A"))

# time difference
new_year = date(2026, 1, 1)
diff = today - new_year
print("days since new year:", diff.days)

tomorrow = today + timedelta(days=1)
print("tomorrow:", tomorrow)

last_week = today - timedelta(weeks=1)
print("last week:", last_week)

# age calculator
birthday = date(2005, 6, 15)
age = (today - birthday).days // 365
print("age:", age)
