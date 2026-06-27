class Marksheet:
    def __init__(self,roll_number,name,math,science,english,hindi,sst):
        self.roll_number = roll_number
        self.name = name
        self.math = math
        self.science = science
        self.english = english
        self.hindi = hindi
        self.sst = sst


    def total_marks(self):
        return self.math+self.science+self.english+self.hindi+self.sst
    def percentage(self):
        return ((self.total_marks())/500)*100
    
    def calculate_grade(self):
        per = self.percentage()

        if per >=90:
            return "A+"
        elif per>=80 and per <90:
            return "A"
        elif per>=70 and per <80:
            return "B"
        elif per>=60 and per <70:
            return "C"
        elif per>=40 and per <60:
            return "D"
        else:
            return "E"
        
    def result(self):
        res = self.calculate_grade()
        return "PASS" if res!="E" else "FAIL"

    def marksheet(self):
        print("roll no. = ",self.roll_number)
        print("Name of student = ",self.name)
        print("Maths = ",self.math)
        print("Science = ",self.science)
        print("English = ",self.english)
        print("Hindi = ",self.hindi)
        print("SST = ",self.sst)
        print("Total marks = ",self.total_marks())
        print("Percentage = ",self.percentage())
        print("Grade of student = ",self.calculate_grade())
        self.result()
        



stud = Marksheet(1101,'akash',85,90,95,60,88)
stud.marksheet()            

        
