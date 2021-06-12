class MyClass:
    def __str__(self):
        return "MyClassの__str__"
    # pass


def printvalue(arg):
    print(arg)

printvalue(1)

various_types = [1, "1", True, [1, 2, 3], (1, ), {'1': 1}, {1}]

# for elem in various_types:
#     print(elem)