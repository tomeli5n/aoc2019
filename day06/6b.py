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
while( count < 700):

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
mapa = {}
graphmap = {}
saltos = []
for orb in orbits:
	center = orb[:3]
	moon = orb[-3:]
	final += distance.get(center)
	graphmap.setdefault(moon,center)
	mapa.setdefault(distance.get(center), moon)

print(final)


#print(graphmap)

count = 0
road1 = ['YOU']
while True:

	_line = graphmap.get(road1[-1])
	if _line == 'COM': break

	road1.append(_line)

road2 = ['SAN']
while True:

	_line = graphmap.get(road2[-1])
	road2.append(_line)

	if _line in road1: 
		joint = _line
		break

	if _line == 'COM': break

del road1[road1.index(joint):]
#print(road1)
#print(road2)

print(len(road1+road2)-3) #- YOU, -SANTA , -1 por conversion nodo a orbita
#347 too high