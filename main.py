from random import randint

#import data modules
import game_data
from game_data import data

# import Art Modules
from art import logo
from art import vs

# import clea function
from replit import clear

POINTS = 1
SIZE = len(data) - 1

NUM1 = randint(1, SIZE)
NUM2 = randint(1, SIZE)

def play_again():
	from random import randint

	#import data modules
	import game_data
	from game_data import data

	# import Art Modules
	from art import logo
	from art import vs

	# import clea function
	from replit import clear

	POINTS = 1
	SIZE = len(data) - 1


	# Choices letter generator and follow count generator

	def choices(nume, compare):
		name = data[nume]["name"]
		description = data[nume]["description"]
		country = data[nume]["country"]
		print(compare + " : ",end = "")
		print(name +", a " +description+" from "+ country)
		return data[nume]["follower_count"]

	# Random list position generator
	NUM1 = randint(1, SIZE)
	NUM2 = randint(1, SIZE)

	# The game start function
	def start():
		global NUM1
		global NUM2
		if NUM1 == NUM2:
			NUM2 = randint(1, SIZE)
		
		choice_a = choices(NUM1, "Compare A")
		print(vs)
		choice_b = choices(NUM2, "Against B")
		who_has_more = input("Who has more between A and B? : ").lower()

		# Error Capture Formullar
		while who_has_more != "a" and who_has_more != "b":
			who_has_more = input("Who has more followers between A and B? : ").lower()
			if who_has_more == "a" or who_has_more == "b":
				break

		# Game logic 
		if choice_a >= choice_b:
			NUM2 = randint(0, SIZE)
			true_answer = "a"
		elif choice_b >= choice_a:
			NUM1 = NUM2
			NUM2 = randint(0, SIZE)
			true_answer = "b"
		
		# End if wrong
		if who_has_more != true_answer:
			return "wrong"



	while 1 > 0:

		print(logo)

		if POINTS - 1 >= 1:
			print(f"Currrent score is {POINTS - 1}")

		answer = start()	
		
		# Gmae Ending Logic
		if answer == "wrong":
			print(f"You lose, you ended with a score of {POINTS - 1} ")
			break
		POINTS += 1

		clear()
	play_againq = "d"
	while play_againq != "y" and play_againq != "n":
		play_againq = input("Do you want to play again? y / n : ")
		if play_againq == "y":
			clear()
			play_again()
		elif play_againq == "n":
			break

play_again()
