from Register import *
from myhdl import *
import random

@block
def testREG():

	#Entradas
	clk = Signal(False)
	we = Signal(True)
	reset = ResetSignal(0, active = 1, async=True)
	w_addr = Signal(modbv(0)[5:])
	a_addr = Signal(modbv(0)[5:])
	b_addr = Signal(modbv(0)[5:])
	data_w = Signal(modbv(0)[32:])

	#Salidas
	read_A = Signal(modbv(0)[32:])
	read_B =  Signal(modbv(0)[32:])

	dut = RegisterFile(clk, reset, we, w_addr, a_addr, b_addr, data_w, read_A, read_B)

	interv = delay(1)

	randomdata = [random.randrange(0, 2**32) for i in range(32)]

	@instance
	def stim():
		# Escritura de la data
		for i in range(32):
			w_addr.next = i
			data_w.next = randomdata[i]
			clk.next = 1
			yield interv
			clk.next = 0
			yield interv

		# Lectura desde el puerto A
		for i in range(32):
			a_addr.next = i
			clk.next = 1
			yield interv
			clk.next = 0
			yield interv

			condicion = (i == 0 and read_A == 0) or (i != 0 and read_A == randomdata[i])
			assert condicion, "ERROR en el registro {}".format(i)
			yield interv

		# Lectura desde el puerto B
		for i in range(32):
			b_addr.next = i
			clk.next = 1
			yield interv
			clk.next = 0
			yield interv

			condicion = (i == 0 and read_B == 0) or (i != 0 and read_B == randomdata[i])
			assert condicion, "ERROR en el registro {}".format(i)
			yield interv

	return dut, stim

test = testREG()
test.config_sim(trace=True)
test.run_sim(1000)
