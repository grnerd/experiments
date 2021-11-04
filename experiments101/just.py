from string import digits
from itertools import product
for passwd in product(digits, repeat=4):
	print("".join(passwd))
