modules = open("1input.txt")
total = 0
for module in modules:
	mass = int(module)

	fuel = int(mass / 3)
	fuel = fuel -2
	total = total + fuel
print(total)