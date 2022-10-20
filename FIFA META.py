'''
COMPARING FIFA CARDS BASED 
ON MOST IMPORTANT STATS
SKILL MOVES, WEAK FOOT
USING PONDERS
'''

anwser = int(input("Do you want to get rating for: \n 1 - GK \n 2 - LB/RB \n 3 - CB \n 4 - CDM \n 5 - CM \n 6 - CAM \n 7 - LW/RW \n 8 - CF/ST \n "))

if anwser == 1:
    for i in range(2):
        print("You will get a GK rating for comparison \n")
        player1_diving = int(input("Player1 DIVING = \n"))
        player1_handling = int(input("Player1 HANDLING = \n"))
        player1_reflexes = int(input("Player1 REFLEXES = \n"))
        player1_positioning = int(input("Player1 POSITIONING = \n"))
        player1_height = int(input("Player1 HEIGHT = \n"))

        rating = int(player1_diving*0.2 + player1_handling*0.2 + player1_reflexes*0.2 + player1_positioning*0.2 + player1_height*0.1)
        print(f"Your GK has a rating of {rating}")
        print("\n")

if anwser == 2:
    for i in range(2):
        print("You will get a FB rating for comparison \n")
        player1_pace = int(input("Player1 PACE = \n"))
        player1_passing = int(input("Player1 PASSING = \n"))
        player1_dribbling = int(input("Player1 DRIBBLING = \n"))
        player1_defending = int(input("Players DEFENDING = \n"))
        player1_physicality = int(input("Player1 PHYSICALITY = \n"))

        rating = int(player1_pace*0.3 + player1_passing*0.2 + player1_dribbling*0.15 + player1_defending*0.2 + player1_physicality*0.15)
        print(f"Your FB has a rating of {rating}")
        print("\n")

if anwser == 3:
    for i in range(2):
        print("You will get a CB rating for comparison \n")
        player1_pace = int(input("Player1 PACE = \n"))
        player1_passing = int(input("Player1 PASSING = \n"))
        player1_defending = int(input("Players DEFENDING = \n"))
        player1_physicality = int(input("Player1 PHYSICALITY = \n"))

        rating = int(player1_pace*0.3 + player1_passing*0.2 + player1_defending*0.3 + player1_physicality*0.2)
        print(f"Your CB has a rating of {rating}")
        print("\n")

if anwser == 4:
    for i in range(2):
        print("You will get a CDM rating for comparison \n")
        player1_pace = int(input("Player1 PACE = \n"))
        player1_passing = int(input("Player1 PASSING = \n"))
        player1_dribbling = int(input("Player1 DRIBBLING = \n"))
        player1_defending = int(input("Player1 DEFENDING = \n"))
        player1_physicality = int(input("Player1 PHYSICALITY = \n"))
        player1_WF = int(input("Player1 WF = \n"))

        rating = input(player1_pace*0.2 + player1_passing*0.15 + player1_dribbling*0.15 + player1_defending*0.20 + player1_physicality*0.20 + player1_WF*2)
        print(f"Your CDM has a rating of {rating}")
        print("\n")

if anwser == 5:
    for i in range(2):
        print("You will get a CM rating for comparison \n")
        player1_pace = int(input("Player1 PACE = \n"))
        player1_shooting = int(input("Player1 SHOOTING = \n"))
        player1_passing = int(input("Player1 PASSING = \n"))
        player1_dribbling = int(input("Player1 DRIBBLING = \n"))
        player1_defending = int(input("Player1 DEFENDING = \n"))
        player1_physicality = int(input("Player1 PHYSICALITY = \n"))
        player1_SM = int(input("Player1 SM = \n"))
        player1_WF = int(input("Player1 WF = \n"))

        rating = input(player1_pace*0.2 + player1_shooting*0.1 + player1_passing*0.15 + player1_dribbling*0.15 + player1_defending*0.15 + player1_physicality*0.05 + player1_SM*2 + player1_WF*2)
        print(f"Your CM has a rating of {rating}")
        print("\n")

if anwser == 6:  
    for i in range(2):  
        print("You will get a CAM rating for comparison \n")
        player1_pace = int(input("Player1 PACE = \n"))
        player1_shooting = int(input("Player1 SHOOTING = \n"))
        player1_passing = int(input("Player1 PASSING = \n"))
        player1_dribbling = int(input("Player1 DRIBBLING = \n"))
        player1_physicality = int(input("Player1 PHYSICALITY = \n"))
        player1_SM = int(input("Player1 SM = \n"))
        player1_WF = int(input("Player1 WF = \n"))

        rating = input(player1_pace*0.15 + player1_shooting*0.15 + player1_passing*0.2 + player1_dribbling*0.15 + player1_physicality*0.05 + player1_SM*3 + player1_WF*3)
        print(f"Your CAM has a rating of {rating}")
        print("\n")

if anwser == 7:
    for i in range(2):
        print("You will get a LW/RW rating for comparison \n")
        player1_pace = int(input("Player1 PACE = \n"))
        player1_shooting = int(input("Player1 SHOOTING = \n"))
        player1_passing = int(input("Player1 PASSING = \n"))
        player1_dribbling = int(input("Player1 DRIBBLING = \n"))
        player1_physicality = int(input("Player1 PHYSICALITY = \n"))
        player1_SM = int(input("Player1 SM = \n"))
        player1_WF = int(input("Player1 WF = \n"))

        rating = input(player1_pace*0.25 + player1_shooting*0.15 + player1_passing*0.15 + player1_dribbling*0.15 + player1_physicality*0.05 + player1_SM*3 + player1_WF*2)
        print(f"Your LW/RW has a rating of {rating}")
        print("\n")

if anwser == 8:
    for i in range(2):
        print("You will get a CF/ST rating for comparison \n")
        player1_pace = int(input("Player1 PACE = \n"))
        player1_shooting = int(input("Player1 SHOOTING = \n"))
        player1_passing = int(input("Player1 PASSING = \n"))
        player1_dribbling = int(input("Player1 DRIBBLING = \n"))
        player1_physicality = int(input("Player1 PHYSICALITY = \n"))
        player1_SM = int(input("Player1 SM = \n"))
        player1_WF = int(input("Player1 WF = \n"))
    
        rating = input(player1_pace*0.2 + player1_shooting*0.2 + player1_passing*0.15 + player1_dribbling*0.15 + player1_physicality*0.05 + player1_SM*3 + player1_WF*2)
        print(f"Your CF/ST has a rating of {rating}")
        print("\n")