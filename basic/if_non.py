# if文でのNoneの取り扱い
a = None  # 「なにも値が入っていない」が入っている

# if a is None:
#     print("a is None!")
# else:
#     print("a has value!")

if not a:
    print("a is None")
