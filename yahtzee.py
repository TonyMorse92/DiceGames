from typing import List

import random


def how_to_play() -> str:
	return """
******************************************************************************
Yahtzee is played like poker hands, but you're trying to collect them all. 
You have X number of turns (it is the number of types of "hands" there are) to 
try and collect them. There are also 3 "chance" scores you can take as backups. 
You get three rolls each time to collect a given "hand".
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

def score_roll(roll: List[int]) -> int:
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
		test()
	else:
		play()
