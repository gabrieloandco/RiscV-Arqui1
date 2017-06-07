from myhdl import *

@block
def AND(data1,data2,dataout):

	@always_comb
	def assign():
		dataout.next = data1 & data2

	return assign

def Main():

	data1,data2,dataout = [Signal(modbv(0)[32:]) for i in range(3)]
	And_inst= AND(data1,data2,dataout)
	And_inst.convert(hdl='Verilog')

if "__main__" == __name__:
	Main()
