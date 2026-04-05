import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


def menu():
    while True:
        print("\n1. Circle")
        print("2. Rectangle")
        print("3. Triangle")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            r = float(input("Radius: "))
            c = Circle(r)
            print("Area:", c.area())
            print("Perimeter:", c.perimeter())

        elif choice == "2":
            a = float(input("Side a: "))
            b = float(input("Side b: "))
            rect = Rectangle(a, b)
            print("Area:", rect.area())
            print("Perimeter:", rect.perimeter())

        elif choice == "3":
            a = float(input("Side a: "))
            b = float(input("Side b: "))
            c = float(input("Side c: "))
            t = Triangle(a, b, c)
            print("Area:", t.area())
            print("Perimeter:", t.perimeter())

        elif choice == "0":
            break

        else:
            print("Invalid choice!")


menu()