from typing import List

import random


hand = []
score = 0


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
	print(how_to_play())
	x = input("Do you want to roll? ")
	if x == "Y":
		dice = roll(6)
		print(dice)
		keep = input("Which numbers do you want to keep? ").split()
		print(f"You kept:  {[dice[int(i) - 1] for i in keep]}")
	else:
		quit()




def roll(n: int) -> List[int]:
	return [random.randint(1,6) for _ in range(n)]

if __name__ == "__main__":
	play()
