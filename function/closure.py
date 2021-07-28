def compute_square(num):
    return num * num


f = compute_square

print(f(10))

function_list = [1, True, f]
print(function_list[-1](10))


# 関数も引数として渡せる
def execute_func(func, param):
    return func(param)


print(execute_func(f, 10))


# 関数をreturnする
def return_func():

    def inner_func():
        print("This is an inner function")

    return inner_func


f = return_func()
print(f)


# Closure：状態をキープした関数をつくることができる
def power(exponent):
    def inner_power(base):
        return base ** exponent
    return inner_power


power_four = power(4)
print(power_four(2))

power_five = power(5)
print(power_five(2))

power_two = power(2)
print(power_two(10))


# 状態が動的
def average():
    nums = []

    def inner_average(num):
        nums.append(num)
        return sum(nums) / len(nums)
    return inner_average


average_nums = average()
print(average_nums(5))
print(average_nums(15))
