
"""
trazar los caminos a traves de listas con tuples inside (coordenadas)


Pasos
-trazar cada cable
-encontrar las coincidencias
-calcular las distancias a cada cruce


"""

import time
start_time = time.time()

#import matplotlib
#matplotlib.use('TkAgg')
#import matplotlib.pyplot as plt



def get_coords(input):
	x=0
	y=0
	cable = [(0,0)]
	for coord in input:
	# coordenadas (x,y)
		#print(coord[:1]) #1 izq
		direccion = coord[:1]
		largo = int(coord[1:])

		if(direccion=="R") : cable.append((x+largo,y))
		if(direccion=="L") : cable.append((x-largo,y))
		if(direccion=="U") : cable.append((x,y+largo))
		if(direccion=="D") : cable.append((x,y-largo))

		x,y = cable[-1]
	return cable


with open("3inputa.txt", 'r') as f:
	raw1 = [(line.rstrip('\n')) for line in f]

cable1 = []
cable1 = get_coords(raw1)

with open("3inputb.txt", 'r') as f:
	raw2 = [(line.rstrip('\n')) for line in f]

cable2 = []
cable2 = get_coords(raw2)

#grafico
# xgraph=[]
# ygraph=[]
# for point in cable1:
# 	xpoint, ypoint = point
# 	xgraph.append(xpoint)
# 	ygraph.append(ypoint)

# plt.plot(xgraph, ygraph, label="line1")
# xgraph=[]
# ygraph=[]
# for point in cable2:
# 	xpoint, ypoint = point
# 	xgraph.append(xpoint)
# 	ygraph.append(ypoint)
# plt.plot(xgraph, ygraph, label="line2")

#buscar cruces
steps1 = steps2 = 0
steps_global = []

for a in range(0, len(cable1)-1):
	x1,y1 = cable1[a]
	x2,y2 = cable1[a+1]
	#print(a)
	steps1 += abs(x2-x1) #acumulo steps1
	steps1 += abs(y2-y1) #acumulo steps1

	for b in range(0, len(cable2)-1):
		x3,y3 = cable2[b]
		x4,y4 = cable2[b+1]
		steps2 += abs(x4-x3) #acumulo steps2
		steps2 += abs(y4-y3) #acumulo steps2


		# cable2 vertical, cable1 horizontal | asumimos que se cruzan uno vertical y otro H
		#  c2vertila                y   está posicionado en el rango-X y lo cruza en Y
		if(x4-x3==0 and y1-y2 == 0 and (min(x1,x2) < x3 < max(x1,x2)) and (min(y3,y4) < y2 < max(y3,y4))):
			parcial1 = steps1 - abs(x2-x1) + abs(x1-x3) #resta actual y suma parcial
			parcial2 = steps2 - abs(y4-y3) + abs(y1-y3)
			steps_total = parcial1+parcial2
			steps_global.append(steps_total)
			#print("bingo 1:",x3,y1,"distance:",abs(x3)+abs(y1), "steps_total",steps_total,parcial1,parcial2)
		
		# c2 horizonal
		if(x1-x2==0 and y3-y4 == 0 and (min(x3,x4) < x1 < max(x3,x4)) and (min(y1,y2) < y3 < max(y1,y2))):
			parcial1 = steps1 - abs(y1-y2) + abs(y1-y3) #resta actual y suma parcial
			parcial2 = steps2 - abs(x4-x3) + abs(x1-x3)
			steps_total = parcial1+parcial2
			steps_global.append(steps_total)
			#print("bingo 2:",x1,y3, "distance:",abs(x1)+abs(y3), "steps_total",steps_total,parcial1,parcial2)
	
	#end for, reset cable
	steps2 = 0
print("--- %s seconds ---" % (time.time() - start_time))
print(min(steps_global))




#print(cable1)
#plt.plot(xgraph, ygraph)
#plt.show()