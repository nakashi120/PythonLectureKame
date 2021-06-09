import time


class Account:

    count = 0

    def __init__(self, balance, name):
        self.balance = balance
        self.name = name
        self.transaction_histroy = []
        self.account_number = Account.count
        Account.count += 1

    def withdraw(self, price):
        if self.balance > price:
            self.balance -= price
            self.show_balance()
            self.add_transaction(-price)

        else:
            print(f"残高不足です。残高：{self.balance}円")

    def deposit(self, price):
        self.balance += price
        self.show_balance()
        self.add_transaction(price)

    def show_balance(self):
        print(f"口座番号：{self.account_number}, 口座名：{self.name}, 口座番号:{self.account_number}, 残高{self.balance}円")

    def add_transaction(self, price):
        transaction = {
            'withdraw/deposit': price,
            'new_balance': self.balance,
            'time': Account.get_time_str()
        }
        self.transaction_histroy.append(transaction)

    @staticmethod
    def get_time_str():
        current_time = time.localtime()
        return "{0.tm_year}年{0.tm_mon}月{0.tm_mday}日{0.tm_hour}時{0.tm_min}分".format(current_time)

    def show_transaction_history(self):
        for transaction in self.transaction_histroy:
            transaction_str_list = []
            for k, v in transaction.items():
                transaction_str_list.append(f"{k}: {v}")
            print(", ".join(transaction_str_list))


satoshi_acount = Account(100, "satoshi")
satoshi_acount.withdraw(10)
satoshi_acount.deposit(100)

print(satoshi_acount.transaction_histroy)
print(Account.get_time_str())

satoshi_acount.show_transaction_history()

