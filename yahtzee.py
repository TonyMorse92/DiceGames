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
		score = 0	
		dice = roll(num_dice)
		print(dice)
		keep = input("Which numbers do you want to keep? ").split()
		kept = [dice[int(i) - 1] for i in keep]
		score = score_roll(kept)
		if score == 0:
			y = input(f" You kept: {kept}, which is not a valid score. Was that correct? ")
			if y == "Y": 	
				print("Roll failed")
				quit()
			else:
				# This would be a goto
				# I guess rolling loop can be separated from the checking.
				pass
		turn_score += score
		x = input("Do you want to roll or hold? ")
		if str(x).upper() == "H":
			keep_rolling = False
		elif str(x).upper() == "R":
			if len(kept) == num_dice:
				num_dice = 6
			else:
				num_dice = num_dice - len(kept)
	print(f"Your score: {turn_score}")
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


def test():
	print(f"""
Roll \t\t\t\t Expected Value \t\t Match?
[2, 2, 3, 4, 4, 6] \t\t 0 \t\t\t\t {score_roll([2, 2, 3, 4, 4, 6]) == 0}
[1, 2, 3, 4, 5, 6] \t\t 1500 \t\t\t\t {score_roll([1, 2, 3, 4, 5, 6]) == 1500}
[1, 2, 3, 4, 5, 2] \t\t 750 \t\t\t\t {score_roll([1, 2, 3, 4, 5, 2]) == 750}
[2, 2, 2, 2, 2, 2] \t\t 800 \t\t\t\t {score_roll([2, 2, 2, 2, 2, 2]) == 800}
[4, 4, 2, 1, 1, 4] \t\t 600 \t\t\t\t {score_roll([4, 4, 2, 1, 1, 4]) == 600}
[2, 2, 2, 2] \t\t\t 400 \t\t\t\t {score_roll([2, 2, 2, 2]) == 400}
[4, 2, 1, 1, 4] \t\t 200 \t\t\t\t {score_roll([4, 2, 1, 1, 4]) == 200}
[2, 2, 1, 2] \t\t\t 300 \t\t\t\t {score_roll([2, 2, 1, 2]) == 300}
[4, 2] \t\t\t\t 0 \t\t\t\t {score_roll([4, 2]) == 0}
[1, 2, 3, 4, 5, 1] \t\t 850 \t\t\t\t {score_roll([1, 2, 3, 4, 5, 1]) == 850}
""")

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

	

	# Check for straights
	roll.sort()
	# Big straight
	if roll == [1, 2, 3, 4, 5, 6]:
		return 1500
	# Small straight
	elif set(roll) == {1, 2, 3, 4, 5} or set(roll) == {2, 3, 4, 5, 6}:
		# There is probably a better way to do this, but just brute check if there
		# was an extra 1 or 5
		if roll.count(1) == 2:
			return 850
		elif roll.count(5) == 2:
			return 800
		else:		
			return 750	
	else:
		return 100 * sum([_ for _ in set(roll) if roll.count(_) >= 3]) +\
			sum([100 * _ * (roll.count(_) - 3) for _ in set(roll) if roll.count(_) >= 3]) +\
			100 * len([_ for _ in roll if _ == 1]) +\
			50 * len([_ for _ in roll if _ == 5])

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
