print("Welcome to the Landscaping Business Game!")

player_name = input("What's your name? ")

print(f"Hi {player_name}, let's start the business.")

money = 0
tools = "teeth"
team = False

while True:
    print(f"You currently have ${money} and are using your {tools}.")

    action = input("What would you like to do today? (work/upgrade/hire) ")

    if action == "work":

        if tools == "teeth":
            print("You spend the day cutting lawns with your teeth and earn $1.")

            money += 1

        elif tools == "rusty scissors":
            print("You spend the day cutting lawns with your rusty scissors and earn $5.")

            money += 5

        elif tools == "lawnmower":
            print("You spend the day cutting lawns with your lawnmower and earn $50.")

            money += 50

        elif tools == "fancy lawnmower":
            print("You spend the day cutting lawns with your fancy lawnmower and earn $100.")

            money += 100

        elif team:
            print("You spend the day cutting lawns with your team of starving students and earn $250.")

            money += 250

    elif action == "upgrade":

        if tools == "teeth" and money >= 5:
            print("You buy a pair of rusty scissors for $5.")

            money -= 5
            tools = "rusty scissors"

        elif tools == "rusty scissors" and money >= 25:
            print("You buy a lawnmower for $25.")

            money -= 25
            tools = "lawnmower"

        elif tools == "lawnmower" and money >= 250:
            print("You buy a fancy battery powered lawnmower for $250.")

            money -= 250
            tools = "fancy lawnmower"

        else:
            print("You cannot upgrade at this time.")

    elif action == "hire" and money >= 500 and not team:
        print("You hire a team of starving students for $500.")

        money -= 500
        team = True

    else:
        print("Invalid action, please try again.")
        
    if team and money >= 1000:
       print("Congratulations! You've won the game. Thank you for Playing!") 