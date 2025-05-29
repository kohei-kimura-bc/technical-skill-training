import re

# 正規表現パターンを定義
pattern = r"\s+"  # 1つ以上の空白文字に一致

# 対象文字列
text = "Python は とても 強力 な 言語 です。"

# splitを使用して分割
result = re.split(pattern, text)

print(f"分割結果: {result}")
