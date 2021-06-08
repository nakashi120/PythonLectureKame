class Car:
    def __init__(self, model_name, mileage, manufacturer):
        self.model_name = model_name
        self.mileage = mileage
        self.manufacturer = manufacturer

    def gas(self):
        print(f"{self.manufacturer}の{self.model_name}（燃費：{self.mileage}）：アクセル全開")

    def breaks(self):
        print(f"{self.manufacturer}の{self.model_name}（燃費：{self.mileage}）：ブレーキ")


if __name__ == '__main__':
    prius = Car("Prius", 30, "Toyota")
    prius.gas()
    prius.breaks()
