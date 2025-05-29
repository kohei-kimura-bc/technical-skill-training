name = input("What is your name?\n")

# 書込みモードでファイルを開く
file = open("example.txt", "w", encoding="utf-8")
file.write("hello, world!\n")
file.write(f"My name is {name}!")
file.close()
