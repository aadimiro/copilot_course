# TODO: Develop a console-based Rock Paper Scissors Lizard Spock game in Python
# Game should be modular, allowing for easy updates or rule changes
# Implement game rules:
# - Scissors decapitate lizard
# - Scissors cuts paper
# - Paper covers rock 
# - Rock crushes lizard 
# - Lizard poisons Spock 
# - Spock smashes scissors 
# - Lizard eats paper 
# - Paper disproves Spock 
# - Spock vaporizes rock 
# - Rock crushes scissors
# Include user input for selecting options and display game results

import random

class RPSLSGame:
	def __init__(self):
		self.rules = {
			"Schere": ["Echse", "Papier"],
			"Papier": ["Stein", "Spock"],
			"Stein": ["Echse", "Schere"],
			"Echse": ["Spock", "Papier"],
			"Spock": ["Schere", "Stein"]
		}

	def determine_winner(self, user_choice, computer_choice):
		if user_choice == computer_choice:
			return "Unentschieden"
		elif computer_choice in self.rules[user_choice]:
			return "Du gewinnst!"
		else:
			return "Computer gewinnt!"

	def get_user_choice(self):
		choices = list(self.rules.keys())
		print("Wähle eine Option:")
		for i, choice in enumerate(choices, 1):
			print(f"{i}. {choice}")
		
		while True:
			user_input = input("Deine Wahl: ").strip().capitalize()
			
			# Überprüfen, ob die Eingabe eine Zahl ist
			if user_input.isdigit():
				index = int(user_input) - 1
				if 0 <= index < len(choices):
					return choices[index]
			
			# Überprüfen, ob die Eingabe ein gültiger Text ist
			elif user_input in choices:
				return user_input
			
			print("Ungültige Eingabe. Bitte versuche es erneut.")

	def get_computer_choice(self):
		return random.choice(list(self.rules.keys()))

	def play_game(self):
		user_choice = self.get_user_choice()
		computer_choice = self.get_computer_choice()
		print(f"Du hast gewählt: {user_choice}")
		print(f"Computer hat gewählt: {computer_choice}")
		result = self.determine_winner(user_choice, computer_choice)
		print(result)

# Spiel starten
if __name__ == "__main__":
	game = RPSLSGame()
	game.play_game()