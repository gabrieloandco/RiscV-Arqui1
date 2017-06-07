from myhdl import *
from Muxes import *
from MBR import * 
from FSM import *

@block
def CPR(clk,reset,DataOutRAM,dirdato,ALUout,Done,datainstruccion,Opcode,PCEN_BHW,Reg_Ok,Address,WE,RE,Ok_PC):

	#Señales
	Demux_MBR= Signal(modbv(0)[32:])
	Demux_Sel = Signal(modbv(0)[1:])
	MBR_go = Signal(modbv(0)[1:])
	Mux5_Sel = Signal(modbv(0)[1:])
    
	

	#Modulos
	Demuxinst = Demux(Demux_Sel,DataOutRAM,Demux_MBR,PCEN_BHW) 

	MBRinst = MBR(Demux_MBR,clk,reset,MBR_go,datainstruccion)

	Mux5inst = Mux2(Mux5_Sel,dirdato,ALUout,Address) 

	fFSMinst = FSM(clk,reset,Opcode,Done,WE,RE,Demux_Sel,Mux5_Sel,MBR_go,Reg_Ok,Ok_PC)

	return instances()

def Main():
	clk = Signal(False)
	reset = ResetSignal(0, active = 1, async=True)
	DataOutRAM = Signal(modbv(0)[32:])	
	dirdato= Signal(modbv(0)[32:])
	Opcode= Signal(modbv(0)[7:])
	ALUout = Signal(modbv(0)[32:])
	Done = Signal(False)
	datainstruccion=Signal(modbv(0)[32:])
	PCEN_BHW = Signal(modbv(0)[32:])
	Reg_Ok  = Signal(False)
	Address = Signal(modbv(0)[32:])
	WE = Signal(False)
	RE = Signal(False)
	Ok_PC = Signal(False)

	CPR_inst=CPR(clk,reset,DataOutRAM,dirdato,ALUout,Done,datainstruccion,Opcode,PCEN_BHW,Reg_Ok,Address,WE,RE,Ok_PC)
	CPR_inst.convert(hdl="Verilog")

if __name__ == "__main__":
	Main()
