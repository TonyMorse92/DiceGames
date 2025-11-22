from typing import List

import random

min_initial_save = 750
min_subsequent_save = 350


def how_to_play() -> str:
	return """
******************************************************************************
Want to have matches of the dice and pop off.
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
[2, 2, 3, 4, 4, 6] \t\t 6 \t\t\t\t {score_roll([2, 2, 3, 4, 4, 6]) == 6}
[1, 2, 3, 4, 5, 6] \t\t 0 \t\t\t\t {score_roll([1, 2, 3, 4, 5, 6]) == 0}
""")

def score_roll(roll: List[int]) -> int:
	return sum([_ for _ in set(roll) if roll.count(_) >= 2])

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
