# 問題1: リストの基本操作
print("問題1: リストの基本操作")

# 1. 空のリストfruits_listを作成してください
fruits_list = []

# 2. append()を使って "apple", "banana", "orange" を順に追加してください
fruits_list.append("apple")
fruits_list.append("banana")
fruits_list.append("orange")

# 3. insert()を使って、インデックス1の位置に "lemon" を挿入してください
fruits_list.insert(1, "lemon")

# 4. remove()を使って "banana" をリストから削除してください
fruits_list.remove("banana")

# 5. pop()を使って最後の要素を削除し、変数last_fruitに代入してください
last_fruit = fruits_list.pop()

# 6. リストの内容と、削除した最後のフルーツを表示してください
print("最終的なフルーツリスト:", fruits_list)
print("削除した最後のフルーツ:", last_fruit)
# 出力:
# 最終的なフルーツリスト: ['apple', 'lemon']
# 削除した最後のフルーツ: orange
