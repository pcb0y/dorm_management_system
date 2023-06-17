import calendar
from datetime import datetime, timedelta


def get_last_day_of_month(year, month):
    _, last_day = calendar.monthrange(year, month)
    return last_day

# 获取当前日期


current_date = datetime.now()
year = 2023
month = 5

last_day = get_last_day_of_month(year, month)
print(f"The last day of the current month is: {last_day}")
