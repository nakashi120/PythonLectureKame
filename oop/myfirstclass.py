class Person:

    num_legs = 2

    # constructor
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def walk(self):
        print(f"{self.name} is walking")

    def run(self):
        print(f"{self.name} is running")


john = Person("John", 28, "male")
taro = Person("Taro", 18, "male")
emma = Person("Emma", 40, "female")

# インスタンス変数
print(john.name)
john.age = 29
print(john.age)
print(john.gender)

john.walk()
emma.walk()
print(type(taro.run()))

john.num_legs = 10
print(john.num_legs)
print(taro.num_legs)
