from myhdl import *
from tope import *
from bram import *
from ClkDriver import *
from ResetDriver import *

import random

@block
def tbTope():
	A_WIDTH = int(input("lineas del simulacion.hex/ Cantidad de bits del addr de la RAM: ")) 
	clk = Signal(False)
	DataInRAM = Signal(modbv(0)[32:])
	reset = ResetSignal(0, active = 1, async=True)
	Address = Signal(modbv(0)[A_WIDTH:])
	WR = Signal(modbv(0)[4:])
	WE = Signal(False)
	RE = Signal(False)
	DataOutRAM = Signal(modbv(0)[32:])
	Done = Signal(False)

	clkinst = ClkDriver(clk)
	#resetinst = ResetDriver(reset)
	braminst = BRAM(clk,Address,DataInRAM,WR,WE,RE,DataOutRAM,Done,A_WIDTH) #hex
	topeinst = tope(clk,reset,DataOutRAM,Done,Address,DataInRAM,WR,WE,RE)

	interv = delay(7)
	
	return instances()


test = tbTope()
test.config_sim(trace=True)
test.run_sim(1000)

