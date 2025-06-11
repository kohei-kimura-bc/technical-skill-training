# 自作モジュールのimport
import calculator

# 実行
print(f"足し算: 10 + 5 = {calculator.add(10, 5)}")
print(f"引き算: 10 - 5 = {calculator.subtract(10, 5)}")
print(f"掛け算: 10 * 5 = {calculator.multiply(10, 5)}")
print(f"割り算: 10 / 5 = {calculator.divide(10, 5)}")
print(f"割り算: 10 / 0 = {calculator.divide(10, 0)}")
