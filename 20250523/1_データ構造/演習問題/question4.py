# 問題5: ショッピングカート機能の実装
print("\n問題5: ショッピングカート機能の実装")

# 1. 空のカートを作成してください
# ここにコードを書いてください
cart = 

# 2. append()を使って、商品を3つ（”apple”, ”banana”, ”orange” ）追加してください
# ここにコードを書いてください
cart = 

print("商品追加後のカート:", cart)

# 3. insert()を使って、インデックス1の位置に"egg"を挿入してください
# ここにコードを書いてください
cart = 

print("商品挿入後のカート:", cart)

# 4. カート内に"banana"が何個あるかをcount()を使ってカウントしてください
# ここにコードを書いてください
item_to_count = "banana"
item_count = 

print(f"{item_to_count}の出現回数:", item_count)

# 5. remove()を使って、bananaをカートから削除してください
# ここにコードを書いてください
cart = 

print("商品削除後のカート:", cart)

# 6. pop()を使って、最後に追加した商品(milk)を取り出してください
# ここにコードを書いてください
popped_item = 

print("取り出した商品:", popped_item)
print("最終的なカート:", cart)
# 期待される出力例:
# 商品追加後のカート: ['apple', 'banana', 'milk']
# 商品挿入後のカート: ['apple', 'egg', 'banana', 'milk']
# bananaの出現回数: 1
# 商品削除後のカート: ['apple', 'egg', 'milk']
# 取り出した商品: milk
# 最終的なカート: ['apple', 'egg']
