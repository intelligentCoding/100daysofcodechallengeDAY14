def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 6, 7, 8, 9, 10))


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


print(calculate(2, add=3, multiply=5))


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        # if we use .get we won't get an error if that kw value is not sent.
        self.model = kw.get("model")


my_car = Car(make="Nissan")
