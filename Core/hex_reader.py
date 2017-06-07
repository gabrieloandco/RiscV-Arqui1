def Reader(A_WIDTH):
	archivo = input("nombre del archivo:  ")
	f = open(archivo, 'r')
	a = []
	i = 0

	for line in f:
		a.append(line.strip('\n'))
		i += 1
		if i== 2**A_WIDTH: #lineas que deseo leer
			break

	f.close()

	block1 = []
	block2 = []
	block3 = []
	block4 = []
	bw1 = []
	bw2 = []
	bw3 = []
	bw4 = []
	j = 0
	for hexa in a:
		bw1.append(hexa[6:8])
		bw2.append(hexa[4:6])
		bw3.append(hexa[2:4])
		bw4.append(hexa[0:2])

	for i in range(4*len(bw1)):

		if i % 4 == 0:
			block1.append(int(bw1[j],16))
			block2.append(int(bw2[j],16))
			block3.append(int(bw3[j],16))
			block4.append(int(bw4[j],16))
			j += 1
		
		else:
			block1.append(0)
			block2.append(0)
			block3.append(0)
			block4.append(0)

	return block1,block2,block3,block4
		


"""
		l = len(binhexa)
		b1 = binhexa[l-8-1:l]
		b2 = binhexa[l-16-1:l-8-1]
		b3 = binhexa[l-24-1:l-16-1]
		b4 = binhexa[l-32-1:l-24-1]
"""

if __name__ == '__main__':
	a,b,c,d = Reader(5)
	for i in range(len(a)):
		print(hex(d[i]) + " " + hex(c[i]) + " " + hex(b[i]) + " " + hex(a[i]))
	print (len(a))







