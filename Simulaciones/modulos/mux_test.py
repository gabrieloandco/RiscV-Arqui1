from myhdl import *
from Multiplexor import *
import random
def tb():
    sel = Signal(False)
    in1 = Signal(modbv(0)[8:])
    in2 = Signal(modbv(0)[8:])
    output = Signal(modbv(0)[8:])

    dut = mux2_1(sel, in1, in2, output)

    interv = delay(7)

    @always(interv)
    def stim():
        in1.next = random.randint(0, 256)
        in2.next = random.randint(0, 256)
        sel.next = random.randint(0, 1)
        #print("{0}, {1}, {2}, {3}".format(sel, in1, in2, output))
    
    return dut, stim

def simulation():
    signals = traceSignals(tb)
    sim = Simulation(signals)
    sim.run(500)
    
simulation()
