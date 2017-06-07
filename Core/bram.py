from myhdl import *	
from hex_reader import *	

@block
def BRAM(clk,addr,di,enstore,we,re,do,done,
           A_WIDTH=5,
           W_WIDTH=32,B_WIDTH=8):
	"""
	"""
	assert len(addr) == A_WIDTH, "Error: Address width mismatch."
	if do is not None:
		assert len(di) == len(do) == W_WIDTH, "Error: Data width mismatch in portA."

	arrayblock1, arrayblock2, arrayblock3, arrayblock4 = Reader(A_WIDTH)	
	
	ramregsblock1 = [Signal(modbv(arrayblock1[i])[B_WIDTH:]) for i in range(0, 2**A_WIDTH)]
	ramregsblock2 = [Signal(modbv(arrayblock2[i])[B_WIDTH:]) for i in range(0, 2**A_WIDTH)]
	ramregsblock3 = [Signal(modbv(arrayblock3[i])[B_WIDTH:]) for i in range(0, 2**A_WIDTH)]
	ramregsblock4 = [Signal(modbv(arrayblock4[i])[B_WIDTH:]) for i in range(0, 2**A_WIDTH)]



	#for addr in range(A_WIDTH):
	#	ramregsblock1.append(Signal(modbv(arrayblock1[addr])[B_WIDTH:]))
	#	ramregsblock2.append(Signal(modbv(arrayblock2[addr])[B_WIDTH:]))
	#	ramregsblock3.append(Signal(modbv(arrayblock3[addr])[B_WIDTH:])
	#	ramregsblock4[addr] =   Signal(modbv(arrayblock4[addr])[B_WIDTH:])


	@always(clk.posedge)
	def write():
		if we==1:
			if enstore == 1:#'0001':
				ramregsblock1[addr].next=di[8:0]
			elif enstore == 2:#'0010':
				ramregsblock2[addr].next=di[8:0]
			elif enstore == 4:#'0100':
				ramregsblock3[addr].next=di[8:0]
			elif enstore == 8:#'1000':
				ramregsblock4[addr].next=di[8:0]
			elif enstore == 3:#'0011':
				ramregsblock1[addr].next=di[8:0]
				ramregsblock2[addr].next=di[16:8]
			elif enstore == 12: #'1100':
				ramregsblock3[addr].next=di[8:0]
				ramregsblock4[addr].next=di[16:8]
			elif enstore == 5:#'0101':
				ramregsblock1[addr].next=di[8:0]
				ramregsblock3[addr].next=di[16:8]
			elif enstore == 10:#'1010':
				ramregsblock2[addr].next=di[8:0]
				ramregsblock4[addr].next=di[16:8]
			elif enstore == 9:#'1001':
				ramregsblock1[addr].next=di[8:0]
				ramregsblock4[addr].next=di[16:8]
			elif enstore == 6:#'0110':
				ramregsblock2[addr].next=di[8:0]
				ramregsblock3[addr].next=di[16:8]
			elif enstore == 7:#'0111':
				ramregsblock1[addr].next=di[8:0]
				ramregsblock2[addr].next=di[16:8]
				ramregsblock3[addr].next=di[25:16]
			elif enstore == 14:#'1110':
				ramregsblock1[addr].next=di[8:0]
				ramregsblock2[addr].next=di[16:8]
				ramregsblock3[addr].next=di[25:16]
			elif enstore == 11:#'1011':
				ramregsblock1[addr].next=di[8:0]
				ramregsblock2[addr].next=di[16:8]
				ramregsblock4[addr].next=di[25:16]
			elif enstore == 13:#'1101':
				ramregsblock1[addr].next=di[8:0]
				ramregsblock3[addr].next=di[16:8]
				ramregsblock4[addr].next=di[25:16]
			elif enstore == 15:#'1111':
				ramregsblock1[addr].next=di[8:0]
				ramregsblock2[addr].next=di[16:8]
				ramregsblock3[addr].next=di[25:16]
				ramregsblock4[addr].next=di[32:25]
	
	

		
	@always(clk.negedge)
	def read():
		if re==1:
			do.next = concat(ramregsblock4[addr],ramregsblock3[addr],ramregsblock2[addr],ramregsblock1[addr])
		if re==0:
			do.next = 0

	@always(clk.posedge)
	def ramnotdone():
		done.next = 0


	@always(clk.negedge)
	def ramdone():
		if re ==1 or we==1:
			done.next = not done


	return instances()
