# 再帰関数（recursive function）:関数内で自身の関数をcallする関数


# 階乗の計算
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(3))


# フィボナッチ数列
def fibonacci_recursive(num):
    if num >= 2:
        return fibonacci_recursive(num - 1) + fibonacci_recursive(num - 2)
    else:
        return num


# print(fibonacci_recursive(6))


# 再帰じゃないフィボナッチ数列
def fibonacci(num):
    if num < 2:
        return num
    else:
        num_1 = 1
        num_2 = 0
        for _ in range(num - 1):
            result = num_2 + num_1
            num_2 = num_1
            num_1 = result
        return result


# print(fibonacci(6))


for i in range(40):
    print(i, fibonacci(i))
