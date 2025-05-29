file = open("example.txt", "r", encoding="utf-8")
print(file.read())
file.close()


# 拡張子に関わらず読み込める
# file = open("1_path_control.py", "r", encoding="utf-8")
# print(file.read())
# file.close()

# 違うディレクトリのファイルも読み込める
# file = open("../../1_モジュール/説明資料/my_module.py", "r", encoding="utf-8")
# print(file.read())
# file.close()
