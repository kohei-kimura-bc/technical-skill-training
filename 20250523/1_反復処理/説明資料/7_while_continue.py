num = 0
while num < 30:
    if num % 2 == 0:
        num += 1
        continue
    print(num)
    num += 1
else:
    print("else:", num)
