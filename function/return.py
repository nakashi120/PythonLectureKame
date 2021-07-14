def get_first_last_word(text):
    text = text.replace(",", "")
    words = text.split()
    return words[0], words[-1]


text = "Hello, My name is Mike"
first, last = get_first_last_word(text)
print(f"first word is '{first}', last word is '{last}'")
