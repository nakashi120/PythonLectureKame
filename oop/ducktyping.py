class Duck:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print("walking...")

    def quack(self):
        print("quack quack...!")

    def fly(self):
        print("Whee!!!")


class Penguin:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print("waliking...")

    def quack(self):
        print("quack quack...?")

    def swim(self):
        print("Swimming!")


def walk_and_quack(duck):
    duck.walk()
    duck.quack()


if __name__ == "__main__":
    donald = Duck("Donald")
    pingu = Penguin("Pingu")
    donald.walk()
    donald.quack()
    pingu.walk()
    pingu.quack()
    walk_and_quack(donald)
    walk_and_quack(pingu)
