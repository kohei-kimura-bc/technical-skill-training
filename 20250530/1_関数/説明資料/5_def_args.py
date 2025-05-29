def sum_func(*args):
    print(args)  # (1,2,3,4,5)
    sum = 0
    for i in args:
        sum += i
    return sum


total = sum_func(1, 2, 3, 4, 5)
print(total)
