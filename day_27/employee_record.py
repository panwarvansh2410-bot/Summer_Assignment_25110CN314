class Employee:

    employees ={}

    def __init__(self,Employee_id,Name,Department,Basic_Salary,Designation,Experience):
        
        self.Employee_id = Employee_id
        self.Name = Name
        self.Department = Department
        self.Basic_Salary = Basic_Salary
        self.Designation = Designation
        self.Experience = Experience
        Employee.employees[self.Employee_id] = self


    def employee_details(self):
        print("Employee_id :",self.Employee_id)
        print("Name :",self.Name)
        print("Department :",self.Department)
        print("Basic salary :",self.Basic_Salary)
        print("Designation :",self.Designation)
        print("Experience :",self.Experience)
        print("Net salary :",self.total_salary())
    
    def total_salary(self):
        HRA = 0.2*self.Basic_Salary
        DA = 0.1*self.Basic_Salary
        PF = 0.12*self.Basic_Salary
        Gross_salary = self.Basic_Salary+HRA+DA
        Net_salary = Gross_salary - PF
        return Net_salary
    
    def ID_search(self,id):
        if id == self.Employee_id:
            self.employee_details()
        else:
            print("NOT found employee")

    def update_details(self,new_department,new_experience,new_salary):
        self.Department = new_department
        self.Experience = new_experience
        self.Basic_Salary = new_salary
                
emp1 = Employee(101,'Prakash','IT',60000,'Sales manager',3)
emp2 =Employee(102,'Aman','HR',50000,'Hiring manager',4)
#emp.employee_details()
#emp.total_salary()
#emp.ID_search(101)
#emp.update_details('HR',4,50000)
#emp.ID_search(101)
Employee.employees[102].employee_details()