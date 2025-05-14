try:
    num = int(input("数値を入力してください\n"))
    result = 10 / num
except ValueError:
    print("数値を入力してください")
# except ZeroDivisionError:
#     print("0で割ることはできません")
else:
    print(result)
finally:
    print("処理終了")
# numに数値を入れる場合は正常終了するが、文字列を入力するとエラーになる
# これをキャッチしたい
