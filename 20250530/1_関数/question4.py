"""
キーワード可変長引数 (**kwargs) の利用
以下の要件を満たす関数 `build_profile` を作成してください：
- 名前 (name) と年齢 (age) を必須引数として受け取ります
- その他の任意のキーワード引数を受け取り、辞書として返します
- 辞書には必須引数の `name` と `age` も含めてください
"""


def build_profile(name, age, **kwargs):
    profile = {"name": name, "age": age}  # 必須引数を辞書に格納
    profile.update(kwargs)  # その他のキーワード引数を辞書に追加
    return profile


# テスト
print(build_profile("田中", 30, hobby="読書", job="エンジニア"))
# 期待される出力: {'name': '田中', 'age': 30, 'hobby': '読書', 'job': 'エンジニア'}
print(build_profile("山田", 25))
# 期待される出力: {'name': '山田', 'age': 25}
