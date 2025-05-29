"""
どういうときに使う？
ファイル名を取得して、先頭に今日の日付を追加する とか
"""

import shutil
from pathlib import Path
from datetime import datetime

# カレントファイルが格納されているディレクトリのパスを取得
base_directory = Path(__file__).parent

# base_directory配下の何かを取得
basic_py = base_directory / "basic.py"
print(basic_py)

today = datetime.today().strftime("%Y%m%d")
print(today)

# ファイル名の先頭に今日の日付を追加
new_file_name = f"{today}_{basic_py.stem}{basic_py.suffix}"
print(new_file_name)
# 文字列をファイルパスに変換
new_file_name = base_directory / new_file_name
print(new_file_name)

# ファイルのコピー
shutil.copy(basic_py, new_file_name)

# ファイルの削除
new_file_name.unlink()

# backupディレクトリを作成
backup_dir = base_directory / "backup"
backup_dir.mkdir(exist_ok=True)

# # backupにファイルを移動
# shutil.move(new_file_name, backup_dir)

# コピーしてから、コピー元のファイルを削除（moveと同じ挙動になるがエラーにならない）
shutil.copy(new_file_name, backup_dir)
new_file_name.unlink()
