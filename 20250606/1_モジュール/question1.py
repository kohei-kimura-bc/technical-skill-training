import re

# テキスト内の電話番号を抽出する処理
text = "連絡先: 090-1234-5678, オフィス: 03-9876-5432, 携帯: 080-5555-7777"

# 電話番号の形式 (XXX-XXXX-XXXX) を示す正規表現パターンを定義
pattern = r"\d{3}-\d{4}-\d{4}"

# テキストをカンマ (,) で分割するためのパターンを定義
pattern1 = r","

# カンマでテキストを分割してリストに格納
splitted_text = re.split(pattern1, text)

# 電話番号を格納するための空リスト（phone_numbers）を初期化
phone_numbers = []

# 分割されたテキストの各要素をループで処理
for i in splitted_text:
    # 各要素に対して正規表現で電話番号形式を検索
    match = re.search(pattern, i)
    # マッチした場合は電話番号をリストに追加(リストに追加するときはappend関数を使用する)
    if match:
        phone_numbers.append(match.group())

# 抽出された電話番号を出力
print("問題1の答え:", phone_numbers)
