# 再帰関数（recursive function)：関数内で自身の関数をcallする関数


def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(3))


def fibonacci_recursive(num):
    if num < 2:
        return num
    else:
        return fibonacci_recursive(num-1) + fibonacci_recursive(num-2)


print(fibonacci_recursive(10))


def fibonacci(n):
    if n < 2:
        return n
    else:
        n_1 = 1
        n_2 = 0
        for _ in range(n-1):
            result = n_2 + n_1
            n_2 = n_1
            n_1 = result
        return result


print(fibonacci(10))

for i in range(30):
    print(i, fibonacci(i))

