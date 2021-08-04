# 再帰関数（recursive function)：関数内で自身の関数をcallする関数


def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)
