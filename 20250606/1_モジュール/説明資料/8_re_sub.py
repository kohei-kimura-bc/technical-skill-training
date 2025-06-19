import re

# 正規表現パターンを定義
pattern = r"\d+"  # 1つ以上の数字に一致

# 対象文字列
text = "今日は2025年6月です。"

# subを使用して置換
result = re.sub(pattern, "XXXX", text)

print(f"置換結果: {result}")
