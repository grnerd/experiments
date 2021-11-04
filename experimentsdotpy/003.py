
import random
user = 0
lap = 0

choice = ['rock', 'paper', 'scissor']


while True:
	user_input = input("Type Rock/Paper/scissor or q to quit: ").lower()
	if user_input == "q":
		break

	if user_input not in choice:
		continue


	random_no = random.randint(0, 2)
	lap_pick = choice[random_no]
	print("Computer picked", lap_pick + ".")

	if user_input == "rock" and lap_pick == "scissor":
		print("You Won")
		user += 1

	elif user_input == "scissor" and lap_pick == "paper":
		print("You Won")
		user += 1

	elif user_input == "paper" and lap_pick == "rock":
		print("You Won")
		user += 1

	else:
		print("You loose")
		lap += 1


print("You won", user, "times.")
print("The computer won", lap, "times.")


'''
import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
'''

