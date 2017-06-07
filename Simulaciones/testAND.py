from myhdl import *
from AND import *
import random

@block
def tbAND():
	data1 = Signal(modbv(0)[32:0])
	data2 = Signal(modbv(0)[32:0])
	dataout = Signal(modbv(0)[32:0])

	dut = AND(data1,data2,dataout)

	interv = delay(5)

	@always(interv)
	def stim():
		data1.next = random.randrange(0, 2**32)
		data2.next = random.randrange(0, 2**32)
		
		condicion = dataout == data1 & data2
		assert condicion, "ERROR"

	return dut, stim

test = tbAND()
test.config_sim(trace=True)
test.run_sim(500)
