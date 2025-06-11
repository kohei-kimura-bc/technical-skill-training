def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    """割り算を行う（ゼロ除算エラーハンドリング付き）"""
    try:
        if b == 0:
            raise ZeroDivisionError("ゼロで割ることはできません")
        return a / b
    except ZeroDivisionError as e:
        return f"エラー: {e}"
