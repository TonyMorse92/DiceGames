import random


def play():
	x = input("Do you want to roll? ")
	if x == "Y":
		for i in range(10):
			print(random.randint(1, 6))
	else:
		quit()





if __name__ == "__main__":
	play()
