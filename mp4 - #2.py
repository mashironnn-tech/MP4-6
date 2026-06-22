
#Name: Byron Ramil B. Pedrialva
#School: FEU-TECH
#Machine Problem number - 2

class Circle:

    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14

    def area(self):
        return self.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * self.pi * self.radius


radius = input("Enter radius:")

try:

    if "." in radius:
        print("You use input whole number value:")

    else:
        radius = int(radius)

        if radius <= 0:
            print("You use enter positive number")

        else:
            circle = Circle(radius)

            print("The answer is", circle.area())
            print("Here is the Answer:", circle.perimeter())

except ValueError:
    print("Invalid input")