class student():
    #attributes
    name = ""
    age = 16
    year = 12
    teacher = ""
    house = "East"

    #constructor function
    def __init__(self):
        print("making a new student...")
    
    def update(self):
        self.age = int(input("what is the student's age? "))
        self.name = str(input("what is the student's name? "))
        self.teacher = str(input("what is the student's teacher? "))
        self.year = int(input("what is the student's year? "))
        self.house = int(input("what is the student's house? "))
        
    def printall(self):
        print("The student's details are")
        print(self.age)
        print(self.name)
        print(self.teacher)
        print(self.year)
        print(self.house)
    
O1 = student()
O1.update()
O1.printall