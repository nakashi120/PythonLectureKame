# コメント
# コメントは常に最新にする。コメントとコードの中身が異なるならコメントはないほうがまし
# なるべく英語で書く。絶対に日本語がわからない人が読まないなら日本語でもOK
# 書くときは文章で書くのが望ましい
# #のあとに半角スペースを入れる
# インラインコメントはコードのあとに半角スペースを2つを入れて書く
# Docstringは基本的にすべてのmodule, function, class, methodにつける
# そのコードが「何をしているか」よりも「なぜそう書いたか」のほうが有益

balance = 10000
withdraw = 1000

# 残高が足りない場合を考慮
if balance < withdraw:
    print("残高が足りません")
