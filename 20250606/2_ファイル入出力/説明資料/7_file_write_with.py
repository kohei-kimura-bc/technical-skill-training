from pathlib import Path

base_dir = Path(__file__).parent
hoge_txt = base_dir / "hoge_dir/hoge.txt"


name = input("What is your name?\n")

# 書込みモードでファイルを開く
with open(hoge_txt, "w", encoding="utf-8") as file:
    file.write("hello, world!\n")
    file.write(f"My name is {name}!")
