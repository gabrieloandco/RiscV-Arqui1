#!/usr/bin/env python

from myhdl import *

@block
def StoreEnable(DWidth,Datain,Store_E):
    assert len(DWidth) == 3, "DWidth no es de 3 bits"
    assert len(Datain) == 2, "Datain no es de 2 bits"

    @always_comb
    def selector():
        """
        Datain son los 2 bits menos significativos de la salida de la ALU.
        A continuacion una tabla indicando todas las posibles combinaciones del ultimo numero 
        hexadecimal de la direccion a la RAM en bits, y para cada uno de ellos la salida sera un enabler de escritura
        de la RAM (enabler de escritura por byte).
        """
        #Byte
        if DWidth == 0b000 or DWidth == 0b011:
            if Datain == 0b00:
                Store_E.next = 0b0001
            elif Datain == 0b01:
                Store_E.next = 0b0010
            elif Datain == 0b10:
                Store_E.next = 0b0100
            elif Datain == 0b11:
                Store_E.next = 0b1000
            else:
                Store_E.next = 0b0000

        #Halfword
        elif DWidth == 0b001 or DWidth == 0b100:
            if Datain == 0b00 or Datain == 0b01:
                Store_E.next = 0b0011
            if Datain == 0b10 or Datain == 0b11:
                Store_E.next = 0b1100
            else:
                Store_E.next = 0b0000

        #Word
        elif DWidth == 0b010:
            Store_E.next = 0b1111
        else:
            Store_E.next = 0b0000
    return selector

"""
sintetizacion a verilog
"""

def convert_StoreE(hdl):

    # Inicialización de las entradas y salidas.
    DWidth = Signal(modbv(0)[3:])
    Datain = Signal(modbv(0)[2:])
    Store_E = Signal(modbv(0)[4:])

    convertSE = StoreEnable(DWidth,Datain,Store_E)
    convertSE.convert(hdl=hdl)

if __name__ == '__main__':

    convert_StoreE(hdl='verilog')
