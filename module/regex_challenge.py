import re


# pattern_dob = '[0-9]{4}/[0-9]{1,2}/[0-9][1,2]'
# pattern_dob = '^(19|20)[0-9]{2}/([1-9]|1[0-2]/([1-9]|1[0-9]|2[0-9]|3[01]))$'
# while True:
#     dob = input("生年月日を入力してください(yyyy/mm/dd): ")
#     result = re.search(pattern_dob, dob)
#     if result:
#         print(f"{dob}は正しい入力です")
#         break
#     else:
#         print(f"{dob}は間違ったフォーマットです")


# pattern_email = '(\w|.|-)?@(\w|.|-).[a-zA-Z]{2}'
pattern_email = '^(\w|.|-)+@(\w|.|-)+\.[a-zA-Z]{2,3}$'
while True:
    email = input(f"emailを入力してください: ")
    result = re.search(pattern_email, email)
    if result:
        print(f"{email}は正しい入力です")
        break
    else:
        print(f"{email}は間違った入力です。")
