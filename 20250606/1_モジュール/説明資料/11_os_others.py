import os

# 環境変数 'Path' を取得
path_directory = os.getenv("Path")
print(f"HOMEディレクトリ: {path_directory}")

print("\n")

# ファイルを削除
file_path = "example.txt"
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{file_path}を削除しました。")
else:
    print(f"{file_path}は存在しません。")

print("\n")

# ディレクトリを巡回
for root, dirs, files in os.walk("/path/to/directory"):
    print(f"現在のディレクトリ: {root}")
    print(f"ディレクトリ一覧: {dirs}")
    print(f"ファイル一覧: {files}")


print("\n")

# OSの名前を取得
os_name = os.name

print(f"OSの名前: {os_name}")
