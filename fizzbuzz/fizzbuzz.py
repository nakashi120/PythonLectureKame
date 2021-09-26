class FizzBuzz:
    def __init__(self, num):
        self.num = num

    def fizzbuzz(self):
        if (self.num % 3) == 0 and (self.num % 5) == 0:
            return 'FizzBuzz'
        elif self.num % 3 == 0:
            return 'Fizz'
        elif self.num % 5 == 0:
            return 'Buzz'
        else:
            return self.num
