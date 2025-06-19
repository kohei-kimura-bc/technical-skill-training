"""
問題2: 以下の機能を持つ「calculator.py」モジュールを作成し、
それをインポートして使用してください

calculator.pyの内容:
- add(a, b): 足し算
- subtract(a, b): 引き算
- multiply(a, b): 掛け算
- divide(a, b): 割り算（ゼロ除算のエラーハンドリング含む）

想定出力:
足し算: 10 + 5 = 15
引き算: 10 - 5 = 5
掛け算: 10 * 5 = 50
割り算: 10 / 5 = 2.0
割り算: 10 / 0 = エラー: ゼロで割ることはできません
"""

# 自作モジュールのimport
import calculator

# 実行
print(f"足し算: 10 + 5 = {calculator.add(10, 5)}")
print(f"引き算: 10 - 5 = {calculator.subtract(10, 5)}")
print(f"掛け算: 10 * 5 = {calculator.multiply(10, 5)}")
print(f"割り算: 10 / 5 = {calculator.divide(10, 5)}")
print(f"割り算: 10 / 0 = {calculator.divide(10, 0)}")
