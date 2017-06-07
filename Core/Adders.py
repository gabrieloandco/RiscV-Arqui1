#!/usr/bin/env python

from myhdl import *

@block
def ADD(datain1,datain2,dataout):

    assert len(datain1) == len(datain2), "entradas de longitud distinta a 32 bits"
    assert len(datain2) == len(dataout), "salida de longitud distinta a 32 bits"

    #suma dos elementos
    @always_comb
    def suma():
        dataout.next = datain1+datain2

    return suma

@block
def ADD_4(datain,dataout):

    assert len(datain) == len(dataout), "entrada o salida de longitud distinta a 32 bits"

    #le suma a un elemento 4
    @always_comb
    def suma():
        dataout.next = datain + 4

    return suma


def convert_ADD(hdl):
   
    #inicializa las entradas y salidas
    datain1 = Signal(modbv(0)[32:0])
    datain2 = Signal(modbv(0)[32:0])
    dataout = Signal(modbv(0)[32:0])

    convertADD = ADD(datain1,datain2,dataout)
    convertADD.convert(hdl=hdl)

def convert_ADD4(hdl):

    #inicializa las entradas y salidas
    datain = Signal(modbv(0)[32:0])
    dataout = Signal(modbv(0)[32:0])

    convertADD4 = ADD_4(datain,dataout)
    convertADD4.convert(hdl=hdl)

if __name__ == '__main__':

	convert_ADD(hdl='verilog')
	convert_ADD4(hdl='verilog')
