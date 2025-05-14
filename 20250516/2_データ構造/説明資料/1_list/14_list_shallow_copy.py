"""
元のリストのシャローコピーを作成
一次元のリストだと元のリストを変更しても、コピーされたオブジェクトは変更されない
"""

drink_list = ["water", "coffee", "tea", "orange juice", "beer", "whiskey"]
copy_drink_list = drink_list.copy()

drink_list[0] = "cola"
print(drink_list)
print(copy_drink_list)

# 二次元のリストはコピーできない・・・

# drink_list = [["water", "coffee", "tea"], ["orange juice", "beer", "whiskey"]]
# copy_drink_list = drink_list.copy()
# drink_list[0][0] = "cola"
# print(drink_list)
# print(copy_drink_list)
