import random
secret_number = random.randint(1,100)


while True:
    user_guess = int(input("Enter your number to be guess :"))
    if user_guess>secret_number:
        print("Sorry this too high")
    elif user_guess<secret_number:
        print("Sorry this too Low")
    else:
        print("Huray! you got the number")
        break
