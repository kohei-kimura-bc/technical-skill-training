"""
元のリストを破壊せずに、欲しい情報を抽出したい
→別の変数を新しく定義し、その変数に対して代入することで解決
"""

drink_list = ["water", "coffee", "tea", "orange juice", "beer", "whiskey"]

# 新しく変数を定義
reversed_drink_list = drink_list
# reversed_drink_list = drink_list.copy()

# 新しく作った変数のみを反転
reversed_drink_list.reverse()

# これでいけそうだが・・・？
print(reversed_drink_list)
print(drink_list)
