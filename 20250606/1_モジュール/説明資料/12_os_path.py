import os

# パスを指定
file_path = "example.txt"

# パスが存在するか確認
exists = os.path.exists(file_path)

print(f"{file_path}は存在しますか？: {exists}")

# パスを結合
directory = "/home/user"
filename = "file.txt"
full_path = os.path.join(directory, filename)

print(f"結合されたパス: {full_path}")

# パスから末尾を取得
file_path = "/home/user/file.txt"
basename = os.path.basename(file_path)

print(f"basename: {basename}")


# ファイル名を分割
file_path = "/home/user/file.txt"
name, ext = os.path.splitext(file_path)

print(f"ファイル名: {name}")
print(f"拡張子: {ext}")

# ホームディレクトリを展開
path = "~/documents/file.txt"
expanded_path = os.path.expanduser(path)

print(f"展開されたパス: {expanded_path}")
