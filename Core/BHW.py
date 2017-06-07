#!/usr/bin/env python

from myhdl import *

@block
def BHW(DWidth, Dir_Data, Datain, Dataout):
    """
    Entradas: DWidth, Dir_Data, Datain.
    Salidas: Dataout.

    Descripcion:
    Este modulo es el encargado de recibir el dato Byte, Halfword o Word en (32bits), realizar alguna extension si es necesario.

    Dir_Data(2 bits): Los 2 LSB de la direccion de dato.
    DWidth(3 bits): Salida de la CU define la longitud del dato a realizar la operacion Load.
    Datain(32bits): Salida de la memoria RAM contiene el dato a guardar el los registros.
    Dataout(32bits): Dato dirigido a los registros para ser guardado.
    """
    data8_0=Signal(modbv(0)[8:])
    data16_8= Signal(modbv(0)[8:])
    data24_16=Signal(modbv(0)[8:])
    data32_24=Signal(modbv(0)[8:])
    data16_0=Signal(modbv(0)[16:])
    data32_16=Signal(modbv(0)[16:])

    @always_comb
    def assign():
        data8_0.next=Datain[8:0]
        data16_8.next=Datain[16:8]
        data24_16.next=Datain[24:16]
        data32_24.next=Datain[32:24]
        data16_0.next=Datain[16:0]
        data32_16.next=Datain[32:16]

    @always_comb
    def behaviorBHW():
        # load Byte
        if DWidth == 0b000:
            if Dir_Data == 0b00:
                Dataout.next = concat(Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7],data8_0)
            elif Dir_Data == 0b01:
                Dataout.next = concat(Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], data16_8)
            elif Dir_Data == 0b10:
                Dataout.next = concat(Datain[23], Datain[23], Datain[23], Datain[23], Datain[23], Datain[23], Datain[23], Datain[23], Datain[23], Datain[23], Datain[23], Datain[23], Datain[23], Datain[23], Datain[23], Datain[23], Datain[23], Datain[23], Datain[23], Datain[23], Datain[23], Datain[23], Datain[23], Datain[23], data24_16)
            elif Dir_Data == 0b11:
                Dataout.next = concat(Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], data32_24)
            else:
                Dataout.next = concat(Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], Datain[7], data8_0)

        # load Halfword
        elif DWidth == 0b001:
            if Dir_Data == 0b00 or Dir_Data == 0b01:
                Dataout.next = concat(Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], data16_0)
            elif Dir_Data == 0b10 or Dir_Data == 0b11:
                Dataout.next = concat(Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], Datain[31], data32_16)
            else:
                Dataout.next = concat(Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], Datain[15], data16_0)

        # load Word
        elif DWidth == 0b010:
            Dataout.next = Datain
    
        # load Byte Unsigned
        elif DWidth == 0b011:
            if Dir_Data == 0b00:
                Dataout.next = concat(bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), data8_0)
            elif Dir_Data == 0b01:
                Dataout.next = concat(bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), data16_8)
            elif Dir_Data == 0b10:
                Dataout.next = concat(bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), data24_16)
            elif Dir_Data == 0b11:
                Dataout.next = concat(bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), data32_24)
            else:
                Dataout.next = concat(bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), data8_0)

        # load Halfword Undigned
        elif DWidth == 0b100:
            if Dir_Data == 0b00 or Dir_Data == 0b01:
                Dataout.next = concat(bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), data16_0)
            elif Dir_Data == 0b10 or Dir_Data == 0b11:
                Dataout.next = concat(bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0),data32_16)
            else:
                Dataout.next = concat(bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), bool(0), data16_0)
        else:
            Dataout.next = Datain

    return instances()

"""
sistetizacion a verilog
"""


def convert_BHW(hdl):

    # Inicialización de las entradas y salidas.
    DWidth = Signal(modbv(0)[3:0])
    Dir_Data = Signal(modbv(0)[2:0])
    Datain = Signal(modbv(0)[32:0])
    Dataout = Signal(modbv(0)[32:0])

    convertBHW = BHW(DWidth, Dir_Data, Datain, Dataout)
    convertBHW.convert(hdl=hdl)

if __name__ == '__main__':

	convert_BHW(hdl='verilog')
 
