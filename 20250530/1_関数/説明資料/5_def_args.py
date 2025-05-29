def sum_func(*args):
    print(*args)  # (1,2,3,4,5)
    return sum(args)  # sum(1,2,3,4,5)


total = sum_func(1, 2, 3, 4, 5)
print(total)
