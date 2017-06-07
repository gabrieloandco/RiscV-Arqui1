from myhdl import *
from Adders import *
import random

@block
def testAdders():
    datain = Signal(modbv(0)[32:])
    datain1 = Signal(modbv(0)[32:])
    datain2 = Signal(modbv(0)[32:])
    dataout1 = Signal(modbv(0)[32:])
    dataout2 = Signal(modbv(0)[32:])

    dut1 = ADD(datain1, datain2, dataout1)
    dut2 = ADD_4(datain, dataout2)

    interv = delay(1)


    @always(interv) 
    def stim():
        datain1.next = random.randint(0, 2**32)
        datain2.next = random.randint(0, 2**32)
        datain.next = random.randint(0, 2**32)

    return dut1, dut2, stim


test = testAdders()
test.config_sim(trace=True)
test.run_sim(1000)
