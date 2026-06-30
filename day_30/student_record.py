students = [
    "101,Aman,90",
    "102,Ravi,85",
    "103,Sita,92"
]

while True:
    print("\n1. Show Records")
    print("2. Search Student")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        for student in students:
            roll, name, marks = student.split(",")
            print("Roll:", roll, "Name:", name, "Marks:", marks)

    elif choice == 2:
        search_name = input("Enter student name: ")

        found = False
        for student in students:
            roll, name, marks = student.split(",")

            if name == search_name:
                print("Record Found")
                print("Roll:", roll)
                print("Name:", name)
                print("Marks:", marks)
                found = True
                break

        if not found:
            print("Student not found")

    elif choice == 3:
        break

    else:
        print("Invalid Choice")