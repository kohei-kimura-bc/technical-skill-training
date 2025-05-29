"""
インデックスを指定して取り出す
インデックスを指定しない場合は末尾の要素が取り出される
元のリストから要素は削除される
"""

drink_list = ["water", "coffee", "tea", "orange juice", "beer", "whiskey"]
water = drink_list.pop(0)
whiskey = drink_list.pop()

print(water, whiskey)
print(drink_list)
