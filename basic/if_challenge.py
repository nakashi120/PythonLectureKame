balance = 1000
withdraw = 10000

withdrawal_limit = 1000000

if withdraw >= withdrawal_limit:
    print(f"Maximum withdraw is {withdrawal_limit}")
elif balance >= withdraw:
    balance -= withdraw
    print(f"Your balance is {balance}")
else:
    print("You don't have money")
