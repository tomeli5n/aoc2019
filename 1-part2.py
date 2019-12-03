modules = open("1input.txt")
total = 0

for module in modules:
	mass = int(module)

	fuel = int(mass / 3)
	fuel = fuel -2
	total = total + fuel

	while(fuel > 0):
		doblefuel = int(fuel / 3)
		doblefuel = doblefuel -2

		if(doblefuel>0):
			total = total + doblefuel
			fuel = doblefuel
		else:
			fuel = 0
			
		print(doblefuel)



print(total)

# 4994281 too low. Se agrega el if>0
# 4994396