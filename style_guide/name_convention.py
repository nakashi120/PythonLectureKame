# 命名規則
# 変数や関数: snake_case ex) balance, image_height
# クラス名: CamelCase ex) Person, MyClass
# モジュールやパッケージ名: なるべく短いlower caseで、必要であればsnake_case ex) time, numpy

# アンダースコア
# _xxx : internal use only
# xxx_ : Pythonですでに使われている単語を使いたいとき
# __xxx: クラスの属性として使うことで名前就職される
# __xxx__: magic methodと呼ばれるものでPythonが特別に設定しているもの。開発差定義することはない。Overrideすることはある。
# _: 最近実行した戻り値や、iteration時に使わない変数

class_ = 1


class MyClass:
    def __init__(self):
        pass

    def __str__(self):
        pass


for _ in range(10):
    print("hello")
