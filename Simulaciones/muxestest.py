from myhdl import *
from muxes import *
import random

@block
def tbMUXES():
	#Entradas mux1
    RegDest = Signal(modbv(0)[4:0])
    in1_Mux1 = Signal(modbv(0)[32:0])
    in2_Mux1 = Signal(modbv(0)[32:0])
    in3_Mux1 = Signal(modbv(0)[32:0])
    in4_Mux1 = Signal(modbv(0)[32:0])
    in5_Mux1 = Signal(modbv(0)[32:0])
    output_Mux1 = Signal(modbv(0)[32:0])

    dut1 = Mux1(RegDest, in1_Mux1, in2_Mux1, in3_Mux1, in4_Mux1, in5_Mux1, output_Mux1)

    interv = delay(7)

    @always(interv)
    def stim1():
        in1_Mux1.next = random.randint(0, 256)
        in2_Mux1.next = random.randint(0, 256)
        in3_Mux1.next = random.randint(0, 256)
        in4_Mux1.next = random.randint(0, 256)
        in5_Mux1.next = random.randint(0, 256)
        RegDest.next = random.randint(0, 4)

	#Entradas mux2
    ALUsrc = Signal(modbv(0)[1:0])
    in1_Mux2 = Signal(modbv(0)[32:0])
    in2_Mux2 = Signal(modbv(0)[32:0])
    output_Mux2 = Signal(modbv(0)[32:0])

    dut2 = Mux2(ALUsrc, in1_Mux2, in2_Mux2, output_Mux2)

    @always(interv)
    def stim2():
        in1_Mux2.next = random.randint(0, 256)
        in2_Mux2.next = random.randint(0, 256)
        ALUsrc.next = random.randint(0, 1)

	#Entradas mux3
    Sel_Mux = Signal(modbv(0)[1:0])
    in1_Mux3 = Signal(modbv(0)[32:0])
    in2_Mux3 = Signal(modbv(0)[32:0])
    output_Mux3 = Signal(modbv(0)[32:0])

    dut3 = Mux3(Sel_Mux, in1_Mux3, in2_Mux3, output_Mux3)

    @always(interv)
    def stim3():
        in1_Mux3.next = random.randint(0, 256)
        in2_Mux3.next = random.randint(0, 256)
        Sel_Mux.next = random.randint(0, 1)

	#Entradas mux4
    PCsrc = Signal(modbv(0)[1:0])
    in1_Mux4 = Signal(modbv(0)[32:0])
    in2_Mux4 = Signal(modbv(0)[32:0])
    output_Mux4 = Signal(modbv(0)[32:0])

    dut4 = Mux4(PCsrc, in1_Mux4, in2_Mux4, output_Mux4)

    @always(interv)
    def stim4():
        in1_Mux4.next = random.randint(0, 256)
        in2_Mux4.next = random.randint(0, 256)
        PCsrc.next = random.randint(0, 1)
        
    return dut1, stim1, dut2, stim2, dut3, stim3, dut4, stim4

test = tbMUXES()
test.config_sim(trace=True)
test.run_sim(500)
