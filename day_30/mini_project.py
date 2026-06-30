jersey_number = []
players = []
runs = []
wickets = []
match_score = []

def add_player():
    jersey_number.append(int(input("Enter jersey NO. of player :")))
    players.append(input("Enter name of player :"))
    runs.append(0)
    wickets.append(0)
    print("player added successfully!!")

def update_runs():
    number = int(input("enter jersey number of player :"))

    choice = [0,1,2,4,6,-1]
    if number not in jersey_number:
        print("Player not found")
        return
    index = jersey_number.index(number)
    while True:
        
            run = int(input("Enter runs(0,1,2,4,6 or -1 to stop): "))

            if run == -1:
                break
            if run in choice:
                runs[index]+=run
            else:
                print("Invalid Run !")
    print(players[index],"total runs =",runs[index]) 


def update_wickets():
    number = int(input("enter jersey number of player :"))
    
    if number not in jersey_number:
        print("player not found")
        return
    index = jersey_number.index(number)

    
    wickets[index]+=1
    print(players[index],"Total wickets =",wickets[index])
    

def match_summary():

    if len(players) == 0:
        print("No Players Available")
        return

    total_runs = 0
    total_wickets = 0

    highest_runs = runs[0]
    highest_scorer = players[0]

    for i in range(len(players)):

        total_runs += runs[i]
        total_wickets += wickets[i]

        if runs[i] > highest_runs:
            highest_runs = runs[i]
            highest_scorer = players[i]

    print("\n----- MATCH SUMMARY -----")
    print("Total Team Runs :", total_runs)
    print("Total Team Wickets :", total_wickets)
    print("Highest Scorer :", highest_scorer)
    print("Highest Runs :", highest_runs)


def player_stat():
    number = int(input("enter a number :"))
    if number not in jersey_number:
        print("player not found")
        return
    index = jersey_number.index(number)
    
        
    print("Runs score by :",players[index],"is",runs[index])
    print("wickets by player :",players[index],"is",wickets[index])    


while True:
    print("\n***** CRICKET MANAGEMENT SYSTEM *****")
    print("1. Add Player")
    print("2. Runs of player")
    print("3. wickets of player")
    print("4. Match sumary")
    print("5. player stat")

    print("6. exit system")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        add_player()
    elif choice == 2:
        update_runs()
    elif choice == 3:
        update_wickets()
    elif choice == 4:
        match_summary()
    elif choice == 5:
        player_stat()
    elif choice == 6:
        
    #elif choice == 6:
        print("THANK YOU")    
        break
    else:
        print("Invalid Choice!")