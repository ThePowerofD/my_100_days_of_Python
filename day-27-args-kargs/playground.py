def add(*args):
    sum = 0 
    for n in args:
        sum = sum + n
    return(sum)

print(add(3,4,5))


def calcualte (n, **kwargs):
    print(kwargs)
    #for key, value in kwargs.items():
    #   print(key)
    #   print(value)

    n+= kwargs["add"]
    n*= kwargs["multiply"]
    print(n)

calcualte(2, add=3, multiply=5)

class Car:
    def __init__(self,**kw):
        self.make = kw["make"]
        self.model = kw.get("model")
        self.wheels = kw.get("color")

my_car = Car(make="Nissan", model="GTR", color="Red")
print(my_car.make)