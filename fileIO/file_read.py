# # for文でループで回す
with open("pep8_introduction.txt") as f:
    for line in f:
        print(line, end="")


# .read()でファイルの中身のすべてをひとつのstringとして返す
# 大きなファイルに対しては行わないようにすること
# 理由：すべてがメモリにのってしまうから
with open("pep8_introduction.txt") as f:
    print(f.read())


# .readline()で１行ずつ取得しstringでかえす
with open("pep8_introduction.txt") as f:
    line = f.readline()
    while line:
        print(line, end="")
        line = f.readline()


# .readlines()ですべての行をlistで返す
with open("pep8_introduction.txt") as f:
    lines = f.readlines()
    print(lines)
