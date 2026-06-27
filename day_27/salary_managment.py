class Salary:
    HRA_rate = 0.2
    DA_rate = 0.1
    PF_rate =0.12

    def __init__(self,basic_salary,employee_id,name):
        self.basic_salary = basic_salary
        self.employee_id = employee_id
        self.name = name

    def total_earnings(self):
        hra = self.HRA_rate*self.basic_salary
        
        da = self.DA_rate*self.basic_salary  
        

        gross_salary = hra + da + self.basic_salary
        return gross_salary
    
    def total_deduction(self):
        pf = self.PF_rate*self.basic_salary
        gross = self.total_earnings()

        if gross <= 50000:
            tax = 0*gross
            
        elif gross>50000 and gross<100000:
            tax = 0.1*gross
            

        else:
            tax = 0.2*gross 
        return tax + pf


    def net_salary(self):
        return self.total_earnings() - self.total_deduction()
    
    def salary_slip(self):
        print("Employee name is :",self.name)
        print("Employee id is :",self.employee_id)
        print("basic salary is :",self.basic_salary)
        print("HRA earning is :",self.basic_salary*self.HRA_rate)
        print("DA earning is :",self.basic_salary*self.DA_rate)
        print("PF deduction is :",self.PF_rate*self.basic_salary)
        print("Net salary is :",self.net_salary())


    
        

sl = Salary(80000,101,"RAJU")
#print(sl.total_earnings())
#sl.total_deduction()
#print(sl.total_deduction()) 
#print(sl.net_salary())
sl.salary_slip()


    

    
        

    