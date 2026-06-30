employee_id = []
Name = []
basic_salary = []
department = []

def add_employee():
    employee_id.append(int(input("enter employee id :")))
    Name.append(input("enter employee name :"))
    basic_salary.append(int(input("enter basic salary of employee :")))
    department.append(input("enter department of employee :"))
    print("Employee added successfully !!")

def employee_records():
    for i in range(0,len(employee_id)):
        print("employee id :",employee_id[i])
        print("employee name :",Name[i])
        print("department of employee :",department[i])
        print("net salary of employee :",calculate_salary(basic_salary[i]))

def calculate_salary(basic_salary):
    hra = 0.2*basic_salary
    print("HRA on basic salary :",hra)
    da = 0.1*basic_salary
    print("DA on basic salary :",da)
    pf = 0.12*basic_salary
    print("PF deduction on basic salary :",pf)
    net_salary = basic_salary+hra+da-pf
    return net_salary

def count_employee():
    return len(employee_id)

def search_employee():
    id = int(input("enter employee_id :"))
    for i in range(0,len(employee_id)):
        if id == employee_id[i]:
            print("employee founded !!")
            print("employee name :",Name[i])
            print("department of employee :",department[i])
            print("net salary of employee :",calculate_salary(basic_salary[i]))
            return
    print("employee not found")


def update():
    if len(employee_id)>0:
        new_basic_salary = int(input("enetr new basic salary :"))
        new_department = input("enter new department :")
        new_name = input("enter name :")
        id = int(input("Enter employee id :"))

        for i in range(len(employee_id)):
            if id == employee_id[i]:
                basic_salary[i] = new_basic_salary
                department[i] = new_department
                Name[i] = new_name
    else:
        print("employee not available")


def delete():
    id = int(input("enter id of employee that to be remove :"))
    for i in range(0,len(employee_id)):
        if id ==employee_id[i]:
            employee_id.remove(employee_id[i])
            Name.remove(Name[i])
            basic_salary.remove(basic_salary[i])
            department.remove(department[i])
            print("employee deleted succesfully !!")
            return
    print("employee not available")    


while True:
    print("\n***** EMPLOYEE MANAGEMENT SYSTEM *****")
    print("1. Add Employee")
    print("2. Employee Record")
    print("3. search employee")
    print("4. update details")
    print("5. Remove employee")
    print("6. Total employee")
    print("7. exit system")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        add_employee()
    elif choice == 2:
        employee_records()
    elif choice == 3:
        search_employee()
    elif choice == 4:
        update()
    elif choice == 5:
        delete()
    elif choice == 6:
        print("Total employee :",count_employee())
    elif choice == 7:
        print("THANK YOU")    
        break
    else:
        print("Invalid Choice!")







 