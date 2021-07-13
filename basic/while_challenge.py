# while challenge問題
age = int(input("何歳ですか？："))
casino_age = 18
game_text = """プレイするゲームを選択してください。
1: ルーレット
2: ブラックジャック
3: ポーカー
"""

if age >= casino_age:
    while True:
        game = int(input(game_text))
        if game == 1:
            print("1: ルーレット")
            break
        elif game == 2:
            print("2: ブラック・ジャック")
            break
        elif game == 3:
            print("3: ポーカー")
            break
        else:
            print("正しく選択してください。")
            continue
else:
    print(f"{casino_age}歳未満はカジノに入ることができません。")
