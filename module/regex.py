import re


# Regular Expression（正規表現 通称RegEx）

# email = "myemail@gmail.com"
# print("@" in email)

# パターンと探索したいパターンを入れる
# matched = re.search('@\w+\.', email)
# if matched:
#     print(matched)
#     print("Matched")
# else:
#     print("Not found!")

# []
# いずれかを含む
match = re.search('[abc]', 'd')
match = re.search('[a-c]', 'a')
match = re.search('[0-9]', 'apple')
print(match)

# ^
# 最初の文字
match = re.search('^[0-9]', 'test0')
print(match)

# {n}
# n回リピート
match = re.search('^[0-9]{4}', '2021/3/31')  # 最初の4文字が数字かどうかの判定
print(match)

# {n,m}
# 最低n回、最高m回数
match = re.search('^[0-9]{2,4}', '21/3/31')  # 最初の2文字以上が数字かどうか〜最初の4文字以上が数字かどうか
print(match)

# $
# 最後の文字
match = re.search('[0-9]{2}$', '2021/5/30')  # 最後の2文字が数字かどうか
print(match)

# *
# 左のパターンを0回以上繰り返す
match = re.search('a*b', 'aaaaab')  # aを0回以上繰り返す + b
match = re.search('a*b', 'c')  # aを0回以上繰り返す + b
print(match)

# +
# 左のパターンを1回以上繰り返す
match = re.search('a+b', 'ab')  # aを1回以上繰り返す + b
print(match)

# ?
# 左のパターンを0回か1回繰り返す
match = re.search('ab?c', 'abbbc')  # aを1回、bを0or1回、cを1回
match = re.search('ab?c', 'ac')  # aを1回、bを0or1回、cを1回
print(match)

# |
# or
match = re.search('abc|123', 'abc')
print(match)

# ()
# グループ
match = re.search('te(x|s)t', 'test')
match = re.search('te(x|s)t', 'text')
match = re.search('te(x|s)t', 'tet')
print(match)

# .
# 任意の一文字
match = re.search('h.t', 'hut')
match = re.search('ht', 'hut')
print(match)

# \
# エスケープ
match = re.search('h\.t', 'h.t')
print(match)

# \w
# [a-zA-Z0-9_] すべてのアルファベット、数字及びアンダースコア
match = re.search('h\wt', 'height')
print(match)
