#1
from datetime import datetime, timedelta

current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)

print("Current date:", current_date)
print("Date 5 days ago:", five_days_ago)

#2
from datetime import datetime, timedelta

today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#3
from datetime import datetime

now = datetime.now()
now_no_microseconds = now.replace(microsecond=0)

print("Original datetime:", now)
print("Without microseconds:", now_no_microseconds)

#4
from datetime import datetime

date1 = datetime(2026, 2, 19, 12, 0, 0)
date2 = datetime(2026, 2, 18, 8, 30, 0)

difference = date1 - date2
seconds = difference.total_seconds()

print("Difference in seconds:", seconds)
