# Name: ROBLES, SAM DAVID KIEL G.
# School: FEU-TECH
# Machine Problem number - 1

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width


while True:
    try:
        length_input = input("Enter Length value:")
        width_input = input("Enter the width of the rectangle:")

        if "." in length_input or "." in width_input:
            print("Input the correct data format is not a Positive integer:")
            continue

        length = int(length_input)
        width = int(width_input)

        if length <= 0 or width <= 0:
            print("The number is not a positives integer:")
            continue

        rectangle = Rectangle(length, width)
        print("The Area of the Rectangle is:", rectangle.compute_area())
        
        break

    except ValueError:
        print("Input the correct data format is not a Positive integer:")
