# 問題3: 文字列分割とリスト操作
print("\n問題3: 文字列分割とリスト操作")
text = "Python,Java,C++,JavaScript,Ruby"

# 1. split()メソッドを使って、文字列をカンマで分割し、リストに変換してください
languages = text.split(",")

# 2. extend()メソッドを使って、["Go", "Swift"]をリストに追加してください
languages.extend(["Go", "Swift"])

# 3. リストのコピーを作成してください (shallowcopy)
languages_copy = languages.copy()

# 4. clear()メソッドを使って、元のリストの内容をクリアしてください
languages.clear()

# 5. 結果を表示してください
print("元のリスト(クリア後):", languages)
print("コピーしたリスト:", languages_copy)
# 出力:
# 元のリスト(クリア後): []
# コピーしたリスト: ['Python', 'Java', 'C++', 'JavaScript', 'Ruby', 'Go', 'Swift']
