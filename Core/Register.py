from myhdl import *

@block
def RegisterFile(clk,reset ,we ,w_addr, a_addr, b_addr, data_w, read_A, read_B):
	'''
    PINES DE ENTRADA:
    clk = Clock
    we = Write Enable
    data_w = Data Write (La data que se escribira)
    w_addr = Write address (Donde se escribira)
    a_addr = A address (Donde quiero leer A)
    b_addr = B Adress
    
    PINES DE SALIDA:
    read_A = Data read from A (Lo que lei de A)
    read_B = Data read from B (Lo que lei de B)
	'''

	assert	len(data_w) <= 32, "Excede los 32 bits"
	regs = [Signal(modbv(0)[32:]) for i in range(32)]
	
	@always_seq(we.posedge, reset = reset)
	def write():

		if w_addr != 0 and we == 1 and reset == 0:
			regs[w_addr].next = data_w

		elif reset == 1:
			regs[0].next = 0
			regs[1].next = 0
			regs[2].next = 0
			regs[3].next = 0
			regs[4].next = 0
			regs[5].next = 0
			regs[6].next = 0
			regs[7].next = 0
			regs[8].next = 0
			regs[9].next = 0
			regs[10].next = 0
			regs[11].next = 0
			regs[12].next = 0
			regs[13].next = 0
			regs[14].next = 0
			regs[15].next = 0
			regs[16].next = 0
			regs[17].next = 0
			regs[18].next = 0
			regs[19].next = 0
			regs[20].next = 0
			regs[21].next = 0
			regs[22].next = 0
			regs[23].next = 0
			regs[24].next = 0
			regs[25].next = 0
			regs[26].next = 0
			regs[27].next = 0
			regs[28].next = 0
			regs[29].next = 0
			regs[30].next = 0
			regs[31].next = 0

		else:
			regs[w_addr].next = regs[w_addr]
	

	@always_comb
	def read():
		if a_addr == 0:
			read_A.next= 0 #devuelve 0 si se pide leer de la direccion 0
		else:
			read_A.next = regs[a_addr]
		
		if b_addr == 0:
			read_B.next=0 #devuelve 0 si se pide leer de la direccion 0
		else:
			read_B.next = regs[b_addr]


	return instances()

def Main():

	data_w,read_A,read_B = [Signal(modbv(0)[32:]) for i in range(3)]
	w_addr, a_addr, b_addr= [Signal(modbv(0)[5:]) for i in range(3)]
	clk,we = [Signal(True) for i in range(2)]
	reset = ResetSignal(0, active = 1, async=True)
	Register_inst= RegisterFile(clk,reset,we,w_addr,a_addr,b_addr,data_w,read_A,read_B)
	Register_inst.convert(hdl="Verilog")

if __name__=="__main__":
	Main()
