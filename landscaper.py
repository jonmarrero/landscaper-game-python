print("Welcome to the Landscaping Business Game!")

player_name = input("What's your name? ")
print(f"Hi {player_name}, let's start the business.")

money = 0
tools = "teeth"
team = False

while True:
    print(f"You currently have ${money} and are using your{tools}.")

    action = input("What would you like to do today? (work/upgrade/hire) ")

    if action == "work":
        if tools == "teeth":
            print("You spend the day cutting lawns with your teeth and earn $1.")

            money += 1