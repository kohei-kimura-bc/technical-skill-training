def sum_func(*args):
    print(*args)  # (1,2,3,4,5)
    sum = 0
    for n in args:
        sum += n
    return sum


total = sum_func(1, 2, 3, 4, 5)
print(total)
