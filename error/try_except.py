def split_bill(price):
    num = input("何人で割り勘しますか？")
    try:
        each = price / int(num)
    except ZeroDivisionError as e:
        print("0で割ることはできません。正しい値を入力してください。")
        print(e)
    # except ValueError:
    #     print("数値で入力してください。")
    else:
        print(f"１人{each}円です。")
    finally:
        print("ご利用ありがとうございます")


if __name__ == "__main__":
    split_bill(10000)
