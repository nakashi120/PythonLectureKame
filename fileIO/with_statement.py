# try:
#     f = open("pep8_introduction.txt")
#
#     # fileオブジェクトはiterable
#     for line in f:
#         print(line, end="")
#
# finally:
#     # openしたらcloseする
#     f.close()

# with statement
with open("pep8_introduction.txt") as f:
    for line in f:
        print(line, end="")


# printは最後の改行コードが入る
# 引数でendを用いることで
# print('hello', end='')
# print('world', end='')
