# whileループ
# count = 0
# while count < 10:
#     print(count)
#     count += 1


# brakeとcontinue
while True:
    age = int(input("あなたは何歳ですか？："))
    if not 0 <= age < 120:
        print("入力された値は正しくありません。")
        continue
    else:
        print(f"あなたは{age}歳です。")
        # print("あたなは{}歳です。".format(age))
        break
