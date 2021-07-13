fruits = ['apple', 'peach', 'grapes', 'banana']

# for else
# for fruit in fruits:
#     choice = input(f"あなたは探しているフルーツは{fruit}ですか？ y/n: ")
#     if choice == "y":
#         print("見つかってよかったですね。")
#         break
#     else:
#         print("そうですか...")
# else:
#     print("お探しのフルーツは見つかりませんでした。")

# while else
# count = 0
# while count < 10:
#     print(count)
#     count += 1
# else:
#     print("countは10未満ではななくなりました。")

balance = 1000
gama_price = 200


while balance >= gama_price:
    choice = input(f"1回{gama_price}円のゲームに参加しますか？（残高：{balance}円）（y/n?）：")
    if choice == "y":
        balance -= gama_price
    elif choice == "n":
        print("また遊びましょう。")
        break
    else:
        print("yかnで答えてください。")
else:
    print(f"あなたの残高は{balance}円です。お金が足りません。")
