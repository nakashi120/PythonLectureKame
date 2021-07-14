# *args
def get_average(*args):
    num = len(args)
    if num == 0:
        return
    total = sum(args)
    return total / num


average = get_average(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(average)


# **kwargs
def kwargs_func(**kwargs):
    print(kwargs)


kwargs_func(param1=10, param2=20)