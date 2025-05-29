# 問題4: ショッピングカート機能の実装
print("\n問題5: ショッピングカート機能の実装")

# 1. 空のカートを作成してください
cart = []

# 2. append()を使って、商品を3つ追加してください
cart.append("apple")
cart.append("banana")
cart.append("milk")

print("商品追加後のカート:", cart)

# 3. insert()を使って、インデックス1の位置に新しい商品"egg"を挿入してください
cart.insert(1, "egg")

print("商品挿入後のカート:", cart)

# 4. カート内のbananaが何個あるかをcount()を使ってカウントしてください
item_to_count = "banana"
item_count = cart.count(item_to_count)

print(f"{item_to_count}の出現回数:", item_count)

# 5. remove()を使って、特定の商品をカートから削除してください
cart.remove("banana")

print("商品削除後のカート:", cart)

# 6. pop()を使って、最後に追加した商品を取り出してください
popped_item = cart.pop()

print("取り出した商品:", popped_item)
print("最終的なカート:", cart)
# 出力例:
# 商品追加後のカート: ['apple', 'banana', 'milk']
# 商品挿入後のカート: ['apple', 'egg', 'banana', 'milk']
# bananaの出現回数: 1
# 商品削除後のカート: ['apple', 'egg', 'milk']
# 取り出した商品: milk
# 最終的なカート: ['apple', 'egg']
