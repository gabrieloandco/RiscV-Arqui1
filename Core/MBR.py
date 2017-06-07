from myhdl import *

@block
def MBR(datain,clk,reset,enable,dataout):

	register= Signal(modbv(0)[32:])

	@always_seq(enable.posedge, reset=reset) #actualizar el registro
	def write():
		if enable==1:
			register.next=datain
		elif reset == 1:
			register.next = 0
		else:
			register.next = register

	@always_comb #leer el registro
	def read():
		dataout.next=register


	return instances()

def Main():
	datain,dataout = [Signal(modbv(0)[32:]) for i in range(2)]
	enable,clk =[Signal(True) for i in range(2)]
	reset = ResetSignal(0, active = 1, async=True)
	MBR_inst= MBR(datain,clk,reset,enable,dataout)
	MBR_inst.convert(hdl="Verilog")

if __name__=="__main__":
	Main()
