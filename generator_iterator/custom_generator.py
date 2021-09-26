# range(10)
def myrange(stop):
    start = 0
    while start < stop:
        yield start
        start += 1


mr = myrange(10)
print(type(mr))

for i in mr:
    print(i)


def even(num):
    while num != 0:
        if num % 2 == 0:
            yield num
        num -= 1


print('===================')
for i in even(10):
    print(i)
