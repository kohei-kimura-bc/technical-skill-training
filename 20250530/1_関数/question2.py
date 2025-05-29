"""
デフォルト引数と戻り値
挨拶を生成する関数
"""


def greet(name, greeting="こんにちは"):
    return f"{greeting}、{name}さん"


# テスト
print(greet("田中さん"))  # 出力: こんにちは、田中さんさん
print(greet("山田さん", "おはようございます"))  # 出力: おはようございます、山田さんさん
