from Register import *
from myhdl import *
import random

def tbtestREG():

    #Entradas
    data_w = Signal(modbv(0)[32:])
    w_addr = Signal(modbv(0)[5:])
    a_addr = Signal(modbv(0)[5:])
    b_addr = Signal(modbv(0)[5:])
    we = Signal(modbv(0)[1:])
    clk = Signal(False)

    #Salidas
    read_A = Signal(modbv(0)[32:])
    read_B =  Signal(modbv(0)[32:])

    dut = RegisterFile(data_w, w_addr, a_addr, b_addr, we, clk, read_A, read_B) #No esta bien organizadas los valores, falta el reset

    interv = delay(5)

    @always(interv)
    def stim():
        for i in range(32):
            we.next = random.randrange(0,1)
            w_addr.next = i
            randomdata = random.randrange(0,2**32)
            data_w.next = randomdata
            a_addr.next = i
            assert (i == 0 and read_A == 0) or (i != 0 and read_A == randomdata), "ERROR en el registro {}".format(i)
            b_addr.next = i
            assert (i == 0 and read_B == 0) or (i != 0 and read_B == randomdata), "ERROR en el registro {}".format(i)

    raise StopSimulation

    return dut, stim

test = tbtestREG()
test.config_sim(trace=True)
test.run_sim(1000)
