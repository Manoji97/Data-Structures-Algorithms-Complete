'''

Three holders for n different sized plates 

small plate should always be above larger 

aim is to find minimum moves required for moving all plates from 1 holder to another using auxilary

Its a Recursion Problem 
'''


def TowerOfHanoi(num_plates, start = "A", end = "C", aux = "B"):
	if num_plates == 1: return print(f"move 1 from {start} - {end}")

	TowerOfHanoi(num_plates - 1, start, aux, end)
	print(f"move 1 from {start} - {end}")
	TowerOfHanoi(num_plates - 1, aux, end, start)


TowerOfHanoi(3)