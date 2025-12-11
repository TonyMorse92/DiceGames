from typing import List

import random


def how_to_play() -> str:
	return """
******************************************************************************
Yahtzee is played like poker hands, but you're trying to collect them all. 
You have 13 turns of 3 rolls each to try and get each category. 
There is also a "chance" score you can take as a backup. 
******************************************************************************
"""

def play():
	turn_score = 0
	print(how_to_play())
	keep_rolling = True
	num_dice = 6
	while keep_rolling:
		dice = roll(num_dice)
		kept = []
		for i in range(3):		
			dice = roll(num_dice)	
			print(f"Dice: {dice}")
			keep = input("Which numbers do you want to keep? ").split()
			for j in keep:
				kept.append(dice[int(j)])
			num_dice = 6 - len(kept)
			print(f"Your score: {kept}")
		keep_rolling = False
	quit()

def print_score_sheet() -> None:
	print(f"""
Category \t\t Amt?
Ones \t\t 1
Twos \t\t 1
Threes \t\t 1
Fours \t\t 1
Fives \t\t 1
Sixes \t\t 1
Three of a Kind \t\t 1
Four of a Kind \t\t 1
Full House \t\t 1
Small Straight \t\t 1
Large Straight \t\t 1
Yahtzee \t\t 1
Chance \t\t 1
""")

# Scores are pretty straightforward, so tests will mostly be 
# "Chance" and then things should be able to be canceled out.
def test():
	pass


def score_roll(roll: List[int], category: str) -> int:
	
	if category == "Ones":	
		return sum([_ for _ in roll if _ == 1])
	elif category == "Twos":
		return sum([_ for _ in roll if _ == 2])
	elif category == "Threes":
		return sum([_ for _ in roll if _ == 3])
	elif category == "Fours":
		return sum([_ for _ in roll if _ == 4])
	elif category == "Fives":
		return sum([_ for _ in roll if _ == 5])
	elif category == "Sixes":
		return sum([_ for _ in roll if _ == 6])
	elif category == "Three of a Kind":
		m = sum([_ * (roll.count(_) - 3) for _ in set(roll) if roll.count(_) >= 3])
		if m > 0:
			return m
		else:
			return -5 # This should eventually check if they are crossing out this cat
	elif category == "Four of a Kind":
		m = sum([_ * (roll.count(_) - 3) for _ in set(roll) if roll.count(_) >= 4])
		if m > 0:
			return m
		else:
			return -5 # This should eventually check if they are crossing out this cat
	elif category == "Small Straight":
		return sum([_ for _ in roll if _ == 6])
	elif category == "Large Straight":
		return sum([_ for _ in roll if _ == 6])
	elif category == "Full House":
		return sum([_ for _ in roll if _ == 6])
	elif category == "Yahtzee":
		return sum([_ for _ in roll if _ == 6])
	elif category == "Chance":
		return sum(roll)

def roll(n: int) -> List[int]:
	return [random.randint(1,6) for _ in range(n)]


def check_mode() -> None:
	x = input("Is this a test (T) or are you playing (P)? ")
	return x

		
if __name__ == "__main__":
	stat = check_mode()
	if stat == "T":
		print_score_sheet()
	else:
		play()
