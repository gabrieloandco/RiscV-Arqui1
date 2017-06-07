from PC import *
from myhdl import *
import random

@block
def testPC():

    #Entradas
    datain = Signal(modbv(0)[32:])
    enable = Signal(False)
    clk = Signal(False)
    reset = ResetSignal(0, active = 1, async=True)

    #Salidas
    dataout = Signal(modbv(0)[32:])

    dut = PC(datain,clk,reset,enable,dataout)

    register = Signal(modbv(0)[32:])

    interv = delay(7)
    
    @instance
    def stim():
        for i in range(32):
            datain.next = random.randrange(0, 2**32)
            enable.next = random.randint(0, 1)
            clk.next = 1
            yield interv
            clk.next = 0
            yield interv
            if enable == 1:
                assert dataout == datain, "ERROR"

    return dut, stim

test = testPC()
test.config_sim(trace=True)
test.run_sim(500)
