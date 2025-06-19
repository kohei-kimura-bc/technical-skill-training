"""
以下のコードでは、文字列を分割してリストに変換し、そのリストに対してさまざまな操作を行います。
操作には、リストの要素の位置を取得したり、リストのコピーを作成したり、要素を追加・削除したりするものがあります。
"""

# 元の文字列
text = "Python,Java,C++,JavaScript,Ruby"

"""
問題1: split()メソッドを使って、文字列をカンマで分割し、リストに変換してください
split()は指定した区切り文字で文字列を分割し、リストを返します。
"""
# カンマで分割してリストに変換(split関数を使用)
languages =  
print("問題1:", languages)  # 想定出力: ['Python', 'Java', 'C++', 'JavaScript', 'Ruby']


"""
問題2: index()メソッドを使って、"JavaScript"の位置を取得してください
index()は指定した要素の位置(インデックス)を返します。
"""
# "JavaScript"のインデックスを取得(index関数を使用)
index_of_JavaScript = 
print("問題2:", index_of_JavaScript)  # 結果: 3


"""
問題3: リストのコピーを作成してください (shallow copy)
copy()メソッドはリストの浅いコピーを作成します。
"""
# リストのコピーを作成(copy関数を使用)
languages_copy =  
print("問題3:", languages_copy)  # ['Python', 'Java', 'C++', 'JavaScript', 'Ruby']


"""
問題4: pop()メソッドを使って、元のリストの最後の要素を削除してください
pop()はリストの指定した位置の要素を削除し、その要素を返します。
指定しない場合は最後の要素を削除します。
"""
# 最後の要素 "Ruby" を削除(pop関数を使用)
#以下にコードを追加

print("問題4:", languages)  # ['Python', 'Java', 'C++', 'JavaScript']


"""
問題5: insert()メソッドを使って、元のリストのインデックス2の位置に "Go" を追加してください
insert()は指定した位置に要素を挿入します。
"""
# インデックス2に "Go" を追加(insert関数を使用)
#以下にコードを追加  

print("問題5:", languages)  # ['Python', 'Java', 'Go', 'C++', 'JavaScript']


"""
結果を表示してください
元のリストとコピーしたリストをそれぞれ表示します。
"""
print("問題6: 元のリスト(操作後):", languages)  # ['Python', 'Java', 'Go', 'C++', 'JavaScript']
print("問題6: コピーしたリスト:", languages_copy)  # ['Python', 'Java', 'C++', 'JavaScript', 'Ruby']


"""
期待される出力:
問題1: ['Python', 'Java', 'C++', 'JavaScript', 'Ruby']
問題2: 3
問題3: ['Python', 'Java', 'C++', 'JavaScript', 'Ruby']
問題4: ['Python', 'Java', 'C++', 'JavaScript']
問題5: ['Python', 'Java', 'Go', 'C++', 'JavaScript']
問題6: 元のリスト(操作後): ['Python', 'Java', 'Go', 'C++', 'JavaScript']
問題6: コピーしたリスト: ['Python', 'Java', 'C++', 'JavaScript', 'Ruby']
"""