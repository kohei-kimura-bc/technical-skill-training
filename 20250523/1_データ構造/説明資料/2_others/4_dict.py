colors = dict(red="赤", blue="青", yellow="黄")

print(colors)

print(colors["red"])
print(colors["blue"])
print(colors["yellow"])


# 要素を追加
colors["green"] = "緑"
print(colors)

# 要素を複数個追加
colors.update({"white": "白", "black": "黒"})
print(colors)
