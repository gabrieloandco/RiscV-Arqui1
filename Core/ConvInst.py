from myhdl import *

@block
def ConvInst(datain,dataout):
	''' convierte a la instruccion deseada dependiendo del opcode
	opcode tipo I: Load:0000011, Aritmeticas:0010011,para JAL:1101111
	opcode tipo S:0100011
	opcode tipo B:1100011
	opcode tipo U:para LUI:0110111, para AUIPC:0010111
	opcode tipo JALR:1100111
	'''
	bit31_11= Signal(modbv(0)[21:])
	bit10_5= Signal(modbv(0)[6:])
	bit4_1= Signal(modbv(0)[4:])
	bit0= Signal(modbv(0)[1:])
	bit11= Signal(modbv(0)[1:])
	bit31_12= Signal(modbv(0)[20:])
	bit31= Signal(modbv(0)[1:])
	bit30_20= Signal(modbv(0)[11:])
	bit19_12= Signal(modbv(0)[8:])
	bit11_0= Signal(modbv(0)[12:])
	bit31_20 = Signal(modbv(0)[12:])

	@always_comb
	def assignment():

		if datain[7:0]==0b0000011 or datain[7:0]==0b0010011 or datain[7:0]==0b1101111:
			''' convierte de instruccion al inmediato de I''' 
			bit31_11.next=concat(datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31])
			bit10_5.next=datain[31:25]
			bit4_1.next=datain[25:21]
			bit0.next=datain[20]
			bit11.next = 0
			bit31_12.next = 0
			bit31.next = 0
			bit30_20.next = 0
			bit19_12.next = 0
			bit11_0.next = 0
			bit31_20.next = 0

		elif datain[7:0]==0b0100011:
			'''convierte de instruccion al inmediato de S'''
			bit31_11.next=concat(datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31])
			bit10_5.next=datain[31:25]
			bit4_1.next=datain[12:8]
			bit0.next=datain[7]
			bit11.next = 0
			bit31_12.next = 0
			bit31.next = 0
			bit30_20.next = 0
			bit19_12.next = 0
			bit11_0.next = 0
			bit31_20.next = 0
		
		elif datain[7:0]==0b1100011:
			'''convierte de instruccion al inmediato de B'''
			bit31_12.next=concat(datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31])
			bit11.next=datain[7]
			bit10_5.next=datain[31:25]
			bit4_1.next=datain[12:8]
			bit0.next=bool(0)
			bit31_11.next = 0
			bit31.next = 0
			bit30_20.next = 0
			bit19_12.next = 0
			bit11_0.next = 0
			bit31_20.next = 0
	

		elif datain[7:0]==0b0110111 or datain[7:0]==0b0010111:
			"""   Obtiene el inmediato para las instrucciones de formato U"""
			bit31.next=datain[31]
			bit30_20.next=datain[31:20]
			bit19_12.next=datain[20:12]
			bit11_0.next=concat(bool(0),bool(0),bool(0),bool(0),bool(0),bool(0),bool(0),bool(0),bool(0),bool(0),bool(0),bool(0))
			bit31_11.next = 0
			bit10_5.next = 0
			bit4_1.next = 0
			bit0.next = 0
			bit11.next = 0
			bit31_12.next = 0
			bit31_20.next = 0 
	
		elif datain[7:0]==0b1100111:
			'''convierte de instruccion a JALR'''
			bit31_11.next=0
			bit10_5.next=0
			bit4_1.next=0
			bit0.next=0
			bit11.next = 0
			bit31_12.next = concat(datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31],datain[31])
			bit31.next = 0
			bit30_20.next = 0
			bit19_12.next = 0
			bit11_0.next = datain[31:20]
			bit31_20.next = 0


		else:
			bit31_11.next = 0
			bit10_5.next = 0
			bit4_1.next = 0
			bit0.next = 0
			bit11.next = 0
			bit31_12.next = 0
			bit31.next = 0
			bit30_20.next = 0
			bit19_12.next = 0
			bit11_0.next = 0
			bit31_20.next = 0

	@always_comb
	def concatenacion():
		
		if datain[7:0]==0b0000011 or datain[7:0]==0b0010011 or datain[7:0]==0b1101111:
			dataout.next=concat(bit31_11,bit10_5,bit4_1,bit0)
	
		elif datain[7:0]==0b0100011:
			dataout.next=concat(bit31_11,bit10_5,bit4_1,bit0)

		elif datain[7:0]==0b1100011:
			dataout.next=concat(bit31_12,bit11,bit10_5,bit4_1,bit0)
	
		elif datain[7:0]==0b0110111 or datain[7:0]==0b0010111:
			dataout.next=concat(bit31,bit30_20,bit19_12,bit11_0)
	
		elif datain[7:0]==0b1100111:
			dataout.next=concat(bit31_12,bit11_0)
		else:
			dataout.next=datain
	
	return instances()

def Main():
	datain,dataout = [Signal(modbv(0)[32:]) for i in range(2)]
	ConvInst_inst= ConvInst(datain,dataout)
	ConvInst_inst.convert(hdl='Verilog')
if __name__=="__main__":
	Main()
