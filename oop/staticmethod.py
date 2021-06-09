class MyClass:

    def mymethod(self):
        print("This is normal method from {}".format(self))

    @staticmethod
    def mystaticmethod():
        print("This is static method")


c = MyClass()
c.mymethod()

MyClass.mystaticmethod()
c.mystaticmethod()
