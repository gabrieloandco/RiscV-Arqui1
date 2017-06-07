from myhdl import *
from bram import *
import random

@block
def tbBRAMsimple():
	A_WIDTH = int(input("Memoria de _ bits:"))
	clk = Signal(False)
	di = Signal(modbv(0)[32:])
	addr = Signal(modbv(0)[A_WIDTH:])
	enstore = Signal(modbv(0)[4:])
	we = Signal(False)
	re = Signal(False)
	do = Signal(modbv(0)[32:])
	done = Signal(False)

	dut = BRAM(clk,addr,di,enstore,we,re,do,done, A_WIDTH)
	interv = delay(7)

	@always(interv)
	def clkgen():
		clk.next = not clk

	
	@always(interv)
	def stim():

		di.next=random.randint(0,2**32-1)	
		addr.next= random.randint(0,2**5-1)
		we.next=1#random.randint(0,2-1)
		re.next=1#random.randint(0,2-1)
		enstore.next=random.choice([1,2,4,8,3,12,15])


	return stim,dut,clkgen


test = tbBRAMsimple()
test.config_sim(trace=True)
test.run_sim(1000)

