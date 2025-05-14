"""
深いコピーは元のオブジェクトのコピーを作成し、元のオブジェクトとは別のオブジェクトを作成する
元のオブジェクトが変更されても、コピーされたオブジェクトは変更されない
"""

import copy  # importについては、第3回研修で説明します

drink_list = [["water", "coffee", "tea"], ["orange juice", "beer", "whiskey"]]
copy_drink_list = copy.deepcopy(drink_list)
drink_list[0][0] = "cola"
print(drink_list)
print(copy_drink_list)
