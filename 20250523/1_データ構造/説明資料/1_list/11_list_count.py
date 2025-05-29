"""
リスト内の要素の数を数える
指定した要素がいくつあるか数え、なければ0が返ってくる
大文字小文字は区別される
"""

drink_list = [
    "water",
    "coffee",
    "tea",
    "orange juice",
    "beer",
    "whiskey",
    "water",
    "water",
]
print(drink_list.count("water"))
print(drink_list.count("Water"))
