class MyClass:

    classmethod_count = 0

    def mymethod(self):
        print("This is normal method from {}".format(self))

    @staticmethod
    def mystaticmethod():
        print("This is static method")

    @classmethod
    def myclassmethod(cls):
        cls.classmethod_count += 1
        print(f"This is class method and now the count is {cls.classmethod_count}")


c = MyClass()
c.mymethod()

MyClass.mystaticmethod()
# c.mystaticmethod()

MyClass.myclassmethod()
MyClass.myclassmethod()
