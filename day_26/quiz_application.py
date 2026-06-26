questions = [
    "Q-1: What is the capital of India?",
    "Q-2: Which planet is known as Red planet?",
    "Q-3: How many constitution are there in world",
]
options = [
    ["Mumbai", "Kolkata", "New Delhi", "Chennai"],
    ["Venus", "Mars", "Jupiter", "Saturn"],
    ["5", "6", "7", "8"],
]
count = 0
for i in range(0, len(questions)):

    print((questions[i]))
    # user_ans = input("enter your answer :")
    for j in range(0, len(options[i])):
        labels = ["A", "B", "C", "D"]
        choices = options[i][j]
        print(labels[j], ":", choices)
    user_ans = input("enter your answer :")
    ans = ["C", "B", "C"]


    if user_ans not in labels:
        print("This is INVALID Choice~")
    
    elif user_ans == ans[i]:
        print("Yes your Answer is Correct !!")
        count += 1
    else:
        print("NO this is Wrong Answer")
   

    


print("Hurrah!! your Score is :", count, "/", len(questions))



