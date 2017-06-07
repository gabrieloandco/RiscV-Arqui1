from StoreEnable import *
from myhdl import *
import random

@block
def testStoreEnable():


    #Entradas
    Datain = Signal(modbv(0)[2:])
    DWidth = Signal(modbv(0)[3:])


    #Salida
    Store_E = Signal(modbv(0)[4:])

    dut = StoreEnable(DWidth, Datain, Store_E )

    interv = delay(5)

    @always(interv)
    def stim():

        DWidth.next = random.randrange(0, 2**3)
        Datain.next = random.randrange(0, 2**2)

        #Byte
        if DWidth == 0b000 or 0b011:
            if Datain == 0b00:
                assert Store_E.next == 0b0001, "Error Byte, DWidth:{0}, Datain:{1}, Store_E:{2}".format(DWidth, Datain, Store_E)
            elif Datain == 0b01:
                assert Store_E.next == 0b0010, "Error Byte, DWidth:{0}, Datain:{1}, Store_E:{2}".format(DWidth, Datain, Store_E)
            elif Datain == 0b10:
                assert Store_E.next == 0b0100, "Error Byte, DWidth:{0}, Datain:{1}, Store_E:{2}".format(DWidth, Datain, Store_E)
            elif Datain == 0b11:
                assert Store_E.next == 0b1000, "Error Byte, DWidth:{0}, Datain:{1}, Store_E:{2}".format(DWidth, Datain, Store_E)
            else:
                assert Store_E.next == 0b0000, "Error Byte, DWidth:{0}, Datain:{1}, Store_E:{2}".format(DWidth, Datain, Store_E)
                

        #Halfword
        elif DWidth == 0b001 or 0b100:
            if Datain == 0b00 or 0b01:
                assert Store_E.next == 0b0011, "Error Halfword, DWidth:{0}, Datain:{1}, Store_E:{2}".format(DWidth, Datain, Store_E)
            if Datain == 0b10 or 0b11:
                assert Store_E.next == 0b1100, "Error Halfword, DWidth:{0}, Datain:{1}, Store_E:{2}".format(DWidth, Datain, Store_E)
            else:
                assert Store_E.next == 0b0000, "Error Halfword, DWidth:{0}, Datain:{1}, Store_E:{2}".format(DWidth, Datain, Store_E)

        #Word
        elif DWidth == 0b010:
            assert Store_E.next == 0b1111, "Error Word, DWidth:{0}, Datain:{1}, Store_E:{2}".format(DWidth, Datain, Store_E)
        else:
            Store_E.next = 0b0000
            assert Store_E.next == 0b0000, "Error Word, DWidth:{0}, Datain:{1}, Store_E:{2}".format(DWidth, Datain, Store_E)

    return dut, stim

test = testStoreEnable()
test.config_sim(trace=True)
test.run_sim(1000)
