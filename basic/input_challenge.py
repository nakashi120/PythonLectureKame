age = int(input("何歳ですか？："))
casino_age = 18
game_text = """プレイするゲームを選択してください。
1: ルーレット
2: ブラックジャック
3: ポーカー
"""

if age >= casino_age:
    game = int(input(game_text))
    if game == 1:
        print("1: ルーレット")
    elif game == 2:
        print("2: ブラック・ジャック")
    elif game == 3:
        print("3: ポーカー")
    else:
        print("正しく選択してください。")
else:
    print("{}歳未満はカジノに入ることができません。".format(casino_age))
