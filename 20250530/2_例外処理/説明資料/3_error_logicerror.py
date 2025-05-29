# 引数として入力された数を足し算したい
# 誤ってyに2をかけてしまっている・・
# 問題なく実行されるが、期待した結果にはならない・・


def sum_number(x, y):
    """引数を足し合わせる"""
    return x + 2 * y


print(sum_number(2, 3))

#単体テストでは以下のようなコードを別途作成し、想定通りの動きをするか確かめる

# import unittest

# class TestSumNumber(unittest.TestCase):
#     def test_sum_number(self):
#         self.assertEqual(sum_number(2, 3), 5)
#         self.assertEqual(sum_number(0, 0), 0)
#         self.assertEqual(sum_number(-1, 1), 0)
#         self.assertEqual(sum_number(10, 20), 30)

# if __name__ == '__main__':
#     unittest.main()