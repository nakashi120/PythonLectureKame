# mutable: 変更可能なオブジェクト list, dict, set
fruits = ['apple', 'peach', 'banana']
print(f"fruitsのIDは{id(fruits)}")
fruits.append('lemon')
print(f"fruitsのIDは{id(fruits)}")

# immutable: 変更不可能なオブジェクト int, float, str, bool, tuple
fruit = 'apple'
print(f"fruitのIDは{id(fruit)}")
fruit += ', lemon'
print(f"fruitのIDは{id(fruit)}")

text_list = []
for i in range(1, 11):
    text_list.append(str(i))

text = "-".join(text_list)
print(text)