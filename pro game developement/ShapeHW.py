class Shapes:
    # attributes
    shape = ""
    width = 12
    height = 12

    def __init__(self):
        print("Making a new shape...")

    def update(self):
        self.shape = input("Is it a rectangle or a triangle (equilatereal) ? ").lower()
        self.width = float(input("What is the shape's width? "))
        self.height = float(input("What is the shape's height? "))

    def area(self):
        if self.shape == "triangle":
            area = (self.width * self.height) / 2
            print("The shape's area is " + str(area))
        elif self.shape == "rectangle":
            area = self.width * self.height
            print("The shape's area is " + str(area))
        else:
            print("Unknown shape type.")

    def perimeter(self):
        if self.shape == "triangle":
            perimeter = 3 * self.width
            print("The shape's perimeter is " + str(perimeter))
        elif self.shape == "rectangle":
            perimeter = 2 * (self.width + self.height)
            print("The shape's perimeter is " + str(perimeter))
        else:
            print("Unknown shape type.")

# Example use
s = Shapes()
s.update()
s.area()
s.perimeter()