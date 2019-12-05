"""
int code machine
"""

with open("2input.txt", 'r') as f:
	raw = [int(line.rstrip('\n')) for line in f]

for verb in range(0,100):

	for noun in range(0,100):
		inputvalues = []
		inputvalues = raw.copy()

		print("test ",noun, verb)
		inputvalues[1] = noun
		inputvalues[2] = verb

		count =0
		for line in inputvalues:

			#print(count, inputvalues[count])	
			
			if((count % 4) == 0): #  es modulo
				#print("posicion ",count, inputvalues[count])
				posvalue1 = inputvalues[(count+1)]
				posvalue2 = inputvalues[(count+2)]
				pos = inputvalues[(count+3)]

				while(max(posvalue1,posvalue2,pos)+1 > len(inputvalues)):
					inputvalues.append(0) # agregar al final!

				value1=inputvalues[posvalue1]
				value2=inputvalues[posvalue2]

				if(line == 1): # suma
					op = value1 + value2

					inputvalues[pos] = op
					#print("posicion ", count, " operacion suma", value1, "(",posvalue1, ") + ",value2 ,"(", posvalue2,")=", op, "(",inputvalues[pos])
					#print("confirmacion: ", inputvalues[pos], "en posicion ", pos)

				elif(line == 2): # 2:multiplicacion
					op = value1 * value2
					#print("resultado",value)
					inputvalues[pos] = op
					#print("posicion ", count, " operacion mult", value1, " * ", value2 ,"=", op)
					#print("confirmacion: ", inputvalues[pos], "en posicion ", pos)

				elif(line == 99):
					#halt
					break

			count = count + 1

		print(inputvalues[0])

		if(inputvalues[0]==19690720):
			print("encontrado","noun",noun,"verb",verb)
			stop()
		inputvalues = []
	#print(inputvalues)
# 125 too low. . estaba sumando la posicion, no el valor en dicha posicion.
# 530607 too low  no estaba reemplazando los valores de la consigna

# 3516593, habia que leer todas las intrucciones.

# buscando: 19690720


# With new_list = my_list, you don't actually have two lists. The assignment just copies the reference to the list, not the actual list, so both new_list and my_list refer to the same list after the assignment.

