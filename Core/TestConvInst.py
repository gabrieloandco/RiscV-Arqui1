from myhdl import *
from ConvInst import *
import random
	
def tbConvInst():
	datain = Signal(modbv(0)[32:])
	#din = Signal(modbv(0)[32:])

	dataout = Signal(modbv(0)[32:])
	#dout = Signal(modbv(0)[32:])

	dut = ConvInst(datain,dataout)

	interv = delay(7)


	@always(interv)
	def stim():
		#hi = bin(random.randint(0,2**25-1))[2:]
		#lo= random.choice(['0000011','0010011','1101111','0100011','1100011','0110111','0010111','11001110'])
		#seed = int(hi+lo,2)
		datain.next= random.randint(0,2**32-1)  #seed
		#din.next = seed
		
		#dout.next =ConvInstCheck(seed)
		#if dout != dataout:
		#	print('lo: ' + lo)
		#	print('datain: ' + str(datain))
		#	print('din: ' + str(din))
		#	print('dataout: ' + str(dataout))
		#	print('dout: ' + str(dout))
		#	assert dout == dataout, 'Theres Something Wrong'
    
	return instances()

test = tbConvInst()
test.config_sim(trace=True)
test.run_sim(1000)
#Arreglar el problema con las tuples: AttributeError: 'tuple' object has no attribute 'config_sim'

