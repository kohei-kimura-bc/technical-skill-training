"""
文字列の中から指定した文字の位置を得る
見つかった位置は、文字列の左から数えて何番目か？を示す（先頭は０）
大文字小文字は区別される

"""

drink_list = ["water", "coffee", "tea", "orange juice", "beer", "whiskey"]

# beerの位置を確認
beer_index = drink_list.index("beer")

# 大文字小文字は区別される
beer_index2 = drink_list.index("Beer")

print(beer_index)

# find()とほぼ同じ
# name = "kimura"
# m_index = name.find("m")
# print(m_index)
