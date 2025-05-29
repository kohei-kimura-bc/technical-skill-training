# daysリストを作成
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# for文を使った反復処理でリストのすべてをprintする
for day in days:
    print(day)


# 規定回数ループするにはrangeを使う
for x in range(10):
    print(x)

# 指定した値の範囲でループ（1つずつ増加）
for x in range(10, 20):
    print(x)

for x in range(0, 20, 2):
    print(x)
