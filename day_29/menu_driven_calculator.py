def Add_numbers(num1,num2):
     return num1+num2

def subtract_numbers(num1,num2):
     return num1-num2

def multiply_numbers(num1,num2):
     return num1*num2

def divide_numbers(num1,num2):
     if num2==0:
          return 'can not determine'
     return num1/num2






while True:

    print("\n Menu Driven Calculator ")
    
    print("1. Add the numbers ")
    print("2. Subtract the numbers ")
    print("3. multiply the numbers ")
    print("4. divide the numbers ")
    print("5. exit the app ")
    choice = input("Enter your choice : ")

    num1 = int(input("Enter the number :"))
    num2 = int(input("Enter the number :"))

    match choice:
            case '1':
                
                print("Result =", Add_numbers(num1, num2))


            case '2':
              print("Result =", subtract_numbers(num1, num2))

            case '3':
                
                print("Result =", multiply_numbers(num1, num2))
                    
            case '4':
                print("Result =", divide_numbers(num1, num2))
            case '5':
                break

            case _:
                print("Invalid choice")

