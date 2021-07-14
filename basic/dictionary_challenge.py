# while challenge問題
age = int(input("何歳ですか？："))
casino_age = 18
game_dict = {
    "1": "ルーレット",
    "2": "ブラックジャック",
    "3": "ポーカー",
}

if age >= casino_age:
    while True:
        print('プレイするゲームを選択してください')
        for num, game_name in game_dict.items():
            print(f"{num}: {game_name}")
        game = input(":")

        if game in game_dict.keys():
            print(f"あなたは{game_dict.get(game)}を選びました")
            break
        else:
            print("正しく選択してください。")
            continue
else:
    print(f"{casino_age}歳未満はカジノに入ることができません。")
