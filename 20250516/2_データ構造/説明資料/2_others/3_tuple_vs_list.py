# リストを定義
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# タイプを確認
print(f"今のタイプは{type(li)}です")

# tuple関数でキャスト
li = tuple(li)

# 中身を確認
print(li)

# 再度タイプを確認
print(f"変更後のタイプは{type(li)}です")
