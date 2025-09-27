class car():
    brand = ""
    model = ""
    colour = ""
    wheels = 0
    doors = 0

    def __init__(self):
        print("making a new car...")

    def update(self):
        self.brand = str(input("What is the car's brand? "))
        self.model = str(input("What is the car's model? "))
        self.colour = str(input("What is the car's colour? "))
        self.wheels = int(input("How many wheels does the car have? "))
        self.doors = int(input("How many doors does the car have? "))
    
    def printall(self):
        print("The car's details are:")
        print(self.brand)
        print(self.model)
        print(self.colour)
        print(self.wheels)
        print(self.doors)

O1 = car()
O1.update()
O1.printall()

O2 = car()
O2.update()
O2.printall()