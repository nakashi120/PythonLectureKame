from car import Car


class Truck(Car):
    def __init__(self, model_name, mileage, manufacturer, max_loadings):
        super().__init__(model_name, mileage, manufacturer)
        self._max_loadings = max_loadings
        self._loadings = 0

    def load(self, weight):
        if weight > 0:
            print(f"{weight}tの荷物を積みました")
            self._loadings += weight

        else:
            if self._loadings <= -weight:
                print(f"{self._loadings}tのすべての荷物をおろしました")
                self._loadings = 0
            else:
                # weightは負の値なので、+=で足し算する
                print(f"{-weight}tの荷物をおろしました")
                self._loadings += weight
        print(f"現在の積載量は{self._loadings}tです。")

        if self._loadings > self._max_loadings:
            print(f"最大積載量は{self._max_loadings}tです。重量オーバー")


isuzu_truck = Truck("トラックA", 6, "いすゞ", 10)
isuzu_truck.load(10)
isuzu_truck.load(100)

