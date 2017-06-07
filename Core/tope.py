from myhdl import *

from Adders import *
from ALU import * 
from AND import *
from BHW import *
from ControlUnit import *
from ConvInst import *
from FSM import *
from MBR import *
from Muxes import *
from CPR import *
from PC import *
from Register import *
from StoreEnable import *

@block
def tope(clk,reset,DataOutRAM,Done,Address,DataInRAM,WR,WE,RE):
	
    
	#Señales
	datainstruccion=Signal(modbv(0)[32:]) #Out:CPR, In:Register,ControlUnit,Inm.
	datainmediato=Signal(modbv(0)[32:]) #Out:Inm, In:Mux3,Mux1,Add1

	mux3_add2= Signal(modbv(0)[32:]) #Out:Mux3, In: Add2
	Sel_Mux = Signal(modbv(0)[1:]) #Out:Control Unit, In:Mux3
	add2_mux4 = Signal(modbv(0)[32:]) #Out:Add2, In:Mux4
	PCsrc = Signal(modbv(0)[1:]) #Out: Control Unit, In: Mux4
	RegWrite = Signal(modbv(0)[1:]) #Out: Control Unit, In: And
	mux4_PC = Signal(modbv(0)[32:]) #Out: Mux4, In:PC
	dirdatos= Signal(modbv(0)[32:]) #Out:PC, In:Add2,Add1,Add4,CPR

	mux1_000 = Signal(modbv(0)[32:]) #Out:Add4, In:Mux1
	mux1_001 = Signal(modbv(0)[32:]) #Out: Add1, In: Mux1
	mux1_010 = Signal(modbv(0)[32:]) #Out: Inm, In: Mux1
	mux1_011 = Signal(modbv(0)[32:]) #Out:BHW, In:Mux1	
	RegDest = Signal(modbv(0)[3:])	#Out:Control Unit, In:Mux1

	rdd=Signal(modbv(0)[32:]) #Out: Mux1, In:Register File
	rd= Signal(modbv(0)[5:])  #Out:Datainstruccion, In:RegisterFile
	rs2=Signal(modbv(0)[5:]) #Out:DataInstruccion, In:Register File
	rs1=Signal(modbv(0)[5:]) #Out:DataInstruccion, In:Register File
	r1d = Signal(modbv(0)[32:]) #Out: Register File, In: ALU
	#r2d = Signal(modbv(0)[32:]) #Out: Register File, In: Mux2, BRAM
	RegEnable = Signal(modbv(0)[1:]) #Out:and, In:Register File

	ALUinA=Signal(modbv(0)[32:]) #Out: Mux2, In: ALU
	ALUsrc=Signal(modbv(0)[1:])#Out: Control Unit, In:Mux2
	ALUout = Signal(modbv(0)[32:]) #Out: Alu, In:Mux1, Mux4, BRAM Data, CPR
	ALUflag = Signal(modbv(0)[1:]) #Out: ALU, In: Control Unit 
	ALUop = Signal(modbv(0)[4:]) #Out: Control Unit, In:BHW, Store Enable

	Dwidth= Signal(modbv(0)[3:]) #Out: Control Unit, In:BHW,Store Enable 
	PCEN_BHW = Signal(modbv(0)[32:]) #Out:CPR, In:BHW
	Reg_OK  = Signal(modbv(0)[1:]) #Out:CPR , In:And

	#Ignorar por el  momento, aqui estaba la bram
	#Address = Signal(modbv(0)[5:]) #Out:PC ENABLE, In:BRAM,
	#DataInRAM = Signal(modbv(0)[32:]) #Out:r2d , In: BRAM
	#WR = Signal(modbv(0)[4:]) #Out: , #In:BRAM, Out:Store Enable
	#WE = Signal(False) #Out: , In:BRAM, Out:PC_Enable
	#RE = Signal(False) #Out: , In:BRAM, Out:PC_Enable
	#Done = Signal(False) #Out:BRAM, In:PCEnable
	#DataOutRAM = Signal(modbv(0)[32:]) #Out:Bram, In: Datoinstruccion, In:PC_Enable

	Ok_PC = Signal(modbv(0)[1:]) #In:PC, Out:PC_Enable
	Opcode = Signal(modbv(0)[7:])
	funct7 = Signal(modbv(0)[7:])
	funct3 = Signal(modbv(0)[3:])
	BHWDIR = Signal(modbv(0)[2:])

    #r2d = DataInRAM 
	@always_comb
	def assign():
		rd.next=datainstruccion[12:7] 
		rs2.next=datainstruccion[25:20] 
		rs1.next=datainstruccion[20:15] 
		mux1_010.next = datainmediato
		Opcode.next = datainstruccion[7:0]
		funct7.next = datainstruccion[32:25]
		funct3.next = datainstruccion[15:12]
		BHWDIR.next = ALUout[2:0]

	#Instances	

	Inm=ConvInst(datainstruccion,datainmediato) #Conversor instruccion-inmediato 

	Mux3inst=Mux3(Sel_Mux,4,datainmediato,mux3_add2) #Multiplexor
	
	Add2inst= ADD(mux3_add2,dirdatos,add2_mux4) #Adder

	Mux4inst = Mux4(PCsrc,ALUout,add2_mux4,mux4_PC) #Multiplexor

	PCinst= PC(mux4_PC,clk,reset,Ok_PC,dirdatos) #Program Counter

	Add4inst = ADD_4(dirdatos,mux1_000) #Add4

	Add1inst = ADD(dirdatos,datainmediato,mux1_001) #Adder
	
	Mux1inst = Mux1(RegDest,mux1_000,mux1_001,mux1_010,mux1_011,ALUout,rdd) #Multiplexor
	
	Mux2inst = Mux2(ALUsrc,DataInRAM,datainmediato,ALUinA) #Multiplexor

	ALUinst = ALU(ALUinA,r1d,ALUop,ALUout,ALUflag) #ALU

	ControlUnitInst = ControlUnit(Opcode,funct7,funct3,ALUflag,RegWrite,RegDest,ALUsrc,ALUop,Dwidth,PCsrc,Sel_Mux) #Control Unit

	BHWinst = BHW(Dwidth,BHWDIR,PCEN_BHW,mux1_011) #BHW 

	StoreEnableinst = StoreEnable(Dwidth,BHWDIR,WR) #Store Enable 
	#Block Ram

	Andinst = AND(RegWrite,Reg_OK,RegEnable) #AND

	RegisterFileinst = RegisterFile(clk,reset,RegEnable,rd,rs1,rs2,rdd,r1d,DataInRAM) #Register File

	CPRinst = CPR(clk,reset,DataOutRAM,dirdatos,ALUout,Done,datainstruccion,Opcode,PCEN_BHW,Reg_OK,Address,WE,RE,Ok_PC) #Control PC

	return instances()

def Main():
	clk = Signal(False) 
	reset = ResetSignal(0, active = 1, async=True)
	DataInRAM = Signal(modbv(0)[32:])
	Address = Signal(modbv(0)[5:])
	WE = Signal(False)
	RE = Signal(False)
	DataOutRAM = Signal(modbv(0)[32:])
	Done = Signal(False)
	WR = Signal(modbv(0)[4:])

	tope_inst=tope(clk,reset,DataOutRAM,Done,Address,DataInRAM,WR,WE,RE)
	tope_inst.convert(hdl="Verilog")

if __name__ == "__main__":
	Main()
