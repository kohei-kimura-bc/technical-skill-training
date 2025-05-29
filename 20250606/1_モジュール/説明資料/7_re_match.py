import re

# 正規表現パターンを定義
pattern = r"\d+"  # 1つ以上の数字に一致

# 対象文字列
text = "今日は2025年6月です。"

# matchを使用して検索
match = re.match(pattern, text)

if match:
    print(f"見つかった部分: {match.group()}")  # マッチした部分を取得
else:
    print("一致する部分はありません。")
