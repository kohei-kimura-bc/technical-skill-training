def sample_function(**kwargs):
    print(kwargs)
    for k in kwargs:
        if k == "name":
            print("name is", kwargs[k])


sample_function(name="kimura", age=18, city="Tokyo")
sample_function(x=1, y=2, z=3)


# def print_menu(**kwargs):
#     for dish, price in kwargs.items():
#         print(f"{dish}:{price}yen")
