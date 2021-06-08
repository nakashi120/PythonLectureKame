# lambda関数（無名関数）


def square(x):
    return x * x


lambda x: x * x


def power(exponent):
    return lambda base: base ** exponent


third_power = power(3)
print(third_power(2))


numbers = [6, 2, 5, 43, 5, 36, 67, 2]
# filter()


filtered_num = filter(lambda num: num % 2, numbers)
print(list(filtered_num))
#
#
# for num in numbers:
#     print(filterfunc(num))

