import random
from game_data import data
from img.images import logo, vs

def welcome():
    print(logo)
    print("\033[1mWelcome to our Game!\033[0m")
    print("\033[3mChoose which option was searched the most on Google.\nCollect as many points as you can, if you fail it's Game Over.\033[0m")
    input("Are you ready to start? Press Enter. ")


def vs_names():
    account_a = random.choice(data)
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    print(f"\033[1m\nCompare A: {account_a['Name']}\033[0m")
    print(vs)
    print(f"\033[1mAgainst B: {account_b['Name']}\n\033[0m")
    return account_a, account_b


def compare_counts(account_a, account_b):
    if account_a["count"] > account_b["count"]:
        return 'A'
    elif account_b["count"] > account_a["count"]:
        return 'B'
    else:
        return 'equal'


def restart():
    while True:
        refresh = input("Would you like to play again? Type 'Y' yes or 'N' no: ").lower()
        if refresh == "y":
            start()
            break
        elif refresh == "n":
            print("Thanks for playing. See you soon !")
            break    
        else:
            print("Invalid input.")


def start():
    end_game = False
    score = 0
    welcome()
    while not end_game:
        account_a, account_b = vs_names()

        guess = input("Who had more searches? Type 'A' or 'B': ").strip().upper()
        result = compare_counts(account_a, account_b)

        if result == 'equal':
            print("\u001b[34;1mIt's a tie! No points awarded.\u001b[0m")
            print(f"\u001b[34;1mA, {account_a["Name"]}: {account_a["count"]} and B, {account_b["Name"]}: {account_b["count"]}\u001b[0m")
        elif guess == result:
            score += 1
            print(f"\u001b[34;1mCorrect! Your current score is: {score}\u001b[0m")
            print(f"\u001b[34;1mA, {account_a["Name"]}: {account_a["count"]} and B, {account_b["Name"]}: {account_b["count"]}\u001b[0m")
        else:
            print(f"\u001b[31mWrong! Your final score is: {score}\u001b[0m")
            print(f"\u001b[31mA, {account_a["Name"]}: {account_a["count"]} and B, {account_b["Name"]}: {account_b["count"]}\u001b[0m")
            end_game = True
            restart()


start()



# While not end_game, the player gets one more vs random question. 
# 		If correctly
# 			Add 1 point to score
			
			

# If wrong
# 	End_game = True
# 	Restart()

# Restart game, yes or no.
