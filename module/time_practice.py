from functools import lru_cache
import time


# .time(): 1970/1/1 秒数が表示(Unix時間)
print(time.time())
# 年数に直す
print(time.time()/(60*60*24*365))


@lru_cache()
def fib(n):
    print(f"fibonacci with {n} is running...")
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


# 処理にかかった時間を計算
before = time.time()
# 処理
print(fib(50))
after = time.time()
print(f"recursive fibonacci took {after - before:.2f} sec.")

# .ctime(): 今のローカル時間を文字列で返す
print(time.ctime())
# .localtime(): 構造化データで返す
localtime = time.localtime()
print(localtime)
print("今の時刻は{0.tm_year}年{0.tm_mon}月です".format(localtime))

# .sleep(secs)
# sec = 10
# print(f"{sec}秒待ってください")
# time.sleep(sec)
# print(f"{sec}秒待ちました")


def timer(func):
    def inner(*args, **kwargs):
        before = time.time()
        func(*args, **kwargs)
        after = time.time()
        print(f"{func.__name__} took {after - before:.2f} sec")
    return inner


@timer
def lazy_func(sec):
    print(f"I'm working so hard...")
    time.sleep(sec)
    print(f"I'm finally done!!")


lazy_func(4)