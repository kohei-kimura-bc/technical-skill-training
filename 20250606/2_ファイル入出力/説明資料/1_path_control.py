from pathlib import Path

# j今のファイルが格納されているディレクトリのパスを取得
base_directory = Path(__file__).parent

print(__file__)
print(base_directory)

# base_directory配下の何かを取得
basic_py = base_directory / "basic.py"
print(basic_py)

# ファイルの存在を確認
print(basic_py.exists())
# ファイル名の取得（拡張子あり）
print(basic_py.name)
# ファイル名の取得（拡張子なし）
print(basic_py.stem)
# ファイルの拡張子のみ取得
print(basic_py.suffix)
