class Person:

    def __init__(self, name, age):
        self.name = name
        self._age = age  # 必ず_をつけること

    # getter
    @property
    def age(self):
        print("get_age called")
        return self._age

    # setter
    @age.setter
    def age(self, age):
        print("set_age called")
        if age < 0:
            print("0以上の値を入れてください")
        else:
            self._age = age

    # propertyデコレータを使わない場合
    # age = property(get_age, set_age)


john = Person("John", 10)
print(john.age)
john.age = 5
print(john.age)