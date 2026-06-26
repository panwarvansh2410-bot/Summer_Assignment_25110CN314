age = int(input("Enter your age: "))
citizen = input("Are you a citizen? (yes/no) :")
Voter_id = (input("Are you having voter id ? (yes/no :)"))

if age >= 18 and citizen == "yes" and Voter_id=="yes":
    print("Eligible to vote")
elif age<=0 and age>=140:
    print("Invalid age")
elif age <18:
    print("not eligible for voting")
else:
    print("not eligible to vote")