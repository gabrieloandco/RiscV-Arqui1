from BHW import *
from myhdl import *
import random

@block
def testBHW():

    #Entradas
    DWidth = Signal(modbv(0)[3:0])
    Dir_Data = Signal(modbv(0)[2:0])
    Datain = Signal(modbv(0)[32:0])

    #Salidas
    Dataout = Signal(modbv(0)[32:0])

    dut = BHW(DWidth, Dir_Data, Datain, Dataout)

    interv = delay(5)
    aux = Signal(modbv(0)[3:0])

    @always(interv)
    def stim():
        Datain.next = random.randrange(0, 2**32)
        
        Dir_Data.next = Dir_Data.next + 1
        aux.next = aux.next + 1
        
        if aux.next >= 4:
        	DWidth.next = DWidth.next + 1
        	aux.next = 0

        if DWidth.next >= 5:
        	DWidth.next = 0

    return dut, stim

test = testBHW()
test.config_sim(trace=True)
test.run_sim(500)
