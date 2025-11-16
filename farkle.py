from typing import List

import random

min_initial_save = 750
min_subsequent_save = 350

dice_pool = 6


def how_to_play() -> str:
	return """
******************************************************************************
You will be asked if you want to roll or hold (excepting the first roll).
Valid answers are "R", "r", "H", or "h". 

[I should just take in one letter and capitalize or lowercase it]. 

After the roll is processed, you will be asked which dice to keep
for your score. Give the index (from 1 to 6) of the dice you want.

For example, if you roll [2 3 2 2 4 6] on your first role, you would want
to keep the three 2's for a score of 200. You would type out 1 3 4 
(with spaces between the numbers but not at the beginning or end).
******************************************************************************
"""

def play():
	score = 0
	print(how_to_play())
	x = input("Do you want to roll? ")
	if x == "Y":
		dice = roll(6)
		print(dice)
		keep = input("Which numbers do you want to keep? ").split()
		kept = [dice[int(i) - 1] for i in keep]
		print(f"You kept:  {kept}")
	
		score += score_roll(kept)	
	
		print(f"score: {score}")	
	else:
		quit()

def test():
	# For the straights, I guess I have to check they're order. So sort them first? 
	# And I guess, small straight only applies to a full 6-die roll? 	
	#x = input("""What do you want to test? 

	#	(1): Failed roll -> [2, 2, 3, 4, 4, 6]
	#	(2): Big Straight -> [1, 2, 3, 4, 5, 6]
	#	(3): Small Straight -> [1, 2, 3, 4, 5, 2]
	#	(4): All same -> [2, 2, 2, 2, 2, 2]
	#	(5): Three of kind -> [4, 4, 2, 1, 1, 4]
		
	#	""")
#	test_roll(int(x)) 
	print(f"""
Roll \t\t\t\t Value \t\t\t Computed Value
[2, 2, 3, 4, 4, 6] \t\t 0 \t\t\t {score_roll([2, 2, 3, 4, 4, 6])}
[1, 2, 3, 4, 5, 6] \t\t 1500 \t\t\t {score_roll([1, 2, 3, 4, 5, 6])}
[1, 2, 3, 4, 5, 2] \t\t 750 \t\t\t {score_roll([1, 2, 3, 4, 5, 2])}
[2, 2, 2, 2, 2, 2] \t\t 800 \t\t\t {score_roll([2, 2, 2, 2, 2, 2])}
[4, 4, 2, 1, 1, 4] \t\t 600 \t\t\t {score_roll([4, 4, 2, 1, 1, 4])}
[2, 2, 2, 2] \t\t\t 400 \t\t\t {score_roll([2, 2, 2, 2])}
[4, 2, 1, 1, 4] \t\t 200 \t\t\t {score_roll([4, 2, 1, 1, 4])}
[2, 2, 1, 2] \t\t\t 300 \t\t\t {score_roll([2, 2, 1, 2])}
[4, 2] \t\t\t 0 \t\t\t {score_roll([4, 2])}
[1, 2, 3, 4, 5, 1] \t\t 850 \t\t\t {score_roll([1, 2, 3, 4, 5, 1])}
""")

def score_roll(roll: List[int]) -> int:
	# Check for straights
	roll.sort()
	if roll == [1, 2, 3, 4, 5, 6]:
		return 1500
	elif set(roll) == {1, 2, 3, 4, 5} or set(roll) == {2, 3, 4, 5, 6}:
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
