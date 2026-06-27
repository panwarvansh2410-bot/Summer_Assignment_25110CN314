class Student:
    def __init__(
        self,
        Roll_Number,
        Name,
        Age,
        Class,
        Marks,
    ):
        self.Roll_Number = Roll_Number
        self.Name = Name
        self.Age = Age
        self.Class = Class
        self.Marks = Marks
        

    def student_details(self):
        print("Roll Number :", self.Roll_Number)
        print("Name        :", self.Name)
        print("Age         :", self.Age)
        print("Class       :", self.Class)
        print("Marks       :", self.Marks)
        print("Grade       :", self.calculate_grade())

    def calculate_grade(self):
        if self.Marks >= 450:
            return "A+"
        elif self.Marks >= 400:
            return "A"
        elif self.Marks >= 350:
            return "B"
        elif self.Marks >= 300:
            return "C"
        else:
            return "Fail"

    def update_details(self, new_name):
        self.Name = new_name

    def roll_numb_search(self, roll_number):
        if self.Roll_Number == roll_number:
            self.student_details()
        else:
            print("Roll number not found")


student1 = Student(1101, "RAM", 16, 11, 234)
# student1.roll_numb_search(1101)
# student1.calculate_grade()
student1.update_details("ravi")
student1.student_details()
