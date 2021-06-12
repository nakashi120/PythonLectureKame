# 変数定義
# 演算子の前後にはスペース
x = 1
y = 1

# wrong
xxx     = 1
y       = 2

# 無駄なスペースを最後に入れない
x = 1


# 関数の引数の「=」の前後にはスペース不要
def complex(real, imag=0.0):
    return magic(r=real, i=imag)


# operatorの周りにスペースを置く
# operatorにpriorityがある場合はスペースを無くす
# correct
x = x + 1
x += 1

x = x*2 - 1
a = x*x + y*y
c = (a+1) * (a-1)

# wrong
x=x+1
x +=1

# カンマのあとにはスペースをいれる
range(1, 11)
a = [1, 2, 3, 4]
b = (1, 2, 3)

# wrong
a = [1,3,4,5]

# カンマのあとに閉じカッコの場合はスペース不要
# correct
foo = (0,)

# wrong
foo = (0, )

# リストの最後にカンマ
# バージョン管理のときによい→余計なものが入らない
FILES = [
    'sample.txt',
    'test.txt',
]

# wrong
# これは意味がない
FILES = ['setup.cfg', 'tox.ini',]

# 行の折り返し
# 引数の頭を揃える
foo = long_function_name(var_one, var_two, var_three,
                         var_four, var_five)


# 関数定義
def long_function_name(
        var_one, var_two, var_three, var_four, var_five):
    print("this is the sample function for long name")


# \で区切って改行する
print("このように表示する文章が長かったりする場合は\
      バックスラッシュで区切ると改行できます")

# 演算子が並ぶほうが見やすい
a = 1000000000000000000000000000 \
    + 10000000000000000000000000 \
    + 10000000000000000000000000 \
    + 101


# それぞれの関数間は２行
def func():
    pass


def func2():
    pass


# classのメッソド間は1行でOK
class MyClass:
    def __init__(self):
        pass

    def sample_method(self):
        pass


# Return
import math


# 条件分岐のreturnは全部書く
def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None

# オブジェクトタイプの確認はisinstance()
# correct
if isinstance(obj, int):
# wrong
if type(obj) is type(1):

# Booleanに比較演算子を使わない
bool_var = True

if bool_var == True:

if bool_var:

# type hint
def greeting(name: str) -> str:
    return "hello " + name
# 一つでもhintをつけたら全てにつける
# Pythonがtypeのチェックをするわけではない
# Pythonは動的型付け言語であることを意識