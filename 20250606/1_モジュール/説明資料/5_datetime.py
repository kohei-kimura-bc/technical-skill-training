import datetime

# 現在の日付を取得
today = datetime.date.today()
print(today)

print(today.year)
print(today.month)
print(today.day)


# 現在の日時を取得
now = datetime.datetime.now()
print(now)

delta = datetime.timedelta(days=7)
one_week_later = now + delta
print(one_week_later)
