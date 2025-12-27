# Dice class for drawing and rolling

# Die? 
class Dice:
	def __init__(self, num):
		self.num = num

	def draw(self):
		print("""------------------
		         |		  | 
                         ------------------
			""")




def draw(num: str):
	
	if num == "one":
		return """
---------
|	| 
|   * 	| 
|	| 
---------
		"""


print(draw("one"))
