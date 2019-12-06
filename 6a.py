"""
6 . total de orbitas
# La estrategia será iterar por la linea y reemplazar cada una con el máximo de orbitas, contando desde com.
"""

with open("6input.txt") as f:
	orbits = [line.rstrip('\n') for line in f]

#print(orbits)

distance = {}
distance.setdefault('COM', 1)


count=0
#print(distance)
while( count < 1000):

	for orb in orbits:
		center = orb[:3]
		moon = orb[-3:]
		step = distance.get(center)
		#print(center, moon, step)
		if step:
			#print("ha")
			distance.setdefault(moon, step+1)


	count +=1
#print(distance)

final= 0
for orb in orbits:
	center = orb[:3]
	moon = orb[-3:]
	final += distance.get(center)

print(final)