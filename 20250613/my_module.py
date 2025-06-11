# ファイル内容を読み込んで表示する関数
def display_file_content(file):
    try:
        with open(file.name, "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except Exception as e:
        return f"エラーが発生しました: {str(e)}"


# 四則演算を行う関数
def arithmetic_operations(a, b, operation):
    try:
        a, b = float(a), float(b)
        if operation == "加算":
            return a + b
        elif operation == "減算":
            return a - b
        elif operation == "乗算":
            return a * b
        elif operation == "除算":
            return a / b if b != 0 else "ゼロで割ることはできません"
        else:
            return "不正な操作です"
    except ValueError:
        return "数値を入力してください"


# 挨拶を返す関数
def greeting(name):
    return f"こんにちは、{name}さん！"
