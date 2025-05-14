"""
remove()
リスト内の指定した値のうち、最初に登場したものを削除する
指定した値が存在しなければValueErrorとなる

del リスト[index]
指定したインデックスの要素を削除する
"""

list = [1, 2, 3, 1, 2, 3, 1, 2, 3]
# 1番最初の1を削除
list.remove(1)
print(list)

# リストのインデックス0を削除
del list[0]
print(list)
