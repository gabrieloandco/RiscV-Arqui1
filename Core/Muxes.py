#!/usr/bin/python

from myhdl import *
"""
Este modulo tiene el fin de unir el codigo de los 4 bloques Mux del esquema, los nombres de las variables estan iguales a las
fijadas en el esquema, y las que el esquema no defina seguiran el formato de tener el mismo nombre en cada modulo seguido de _#.
"""
#Mux1 es de 5 a 1 y su selector es la variable definida como RegDest.
@block
def Mux1(RegDest, in1_Mux1, in2_Mux1, in3_Mux1, in4_Mux1, in5_Mux1, output_Mux1):
    
     #assert len(in1_Mux1) == len(in2_Mux1), "Ancho de entrada 1 y 2 distintos"
     #assert len(in2_Mux1) == len(in3_Mux1), "Ancho de entrada 2 y 3 distintos"
     #assert len(in3_Mux1) == len(in4_Mux1), "Ancho de entrada 3 y 4 distintos"
     #assert len(in4_Mux1) == len(in5_Mux1), "Ancho de entrada 4 y 5 distintos"
     #assert len(in4_Mux1) == len(output_Mux1), "Ancho de entrada 5 y output distintos"

    @always_comb
    def behavior_Mux1():
        if RegDest == 0b000:
            output_Mux1.next = in1_Mux1
        elif RegDest == 0b001:
            output_Mux1.next = in2_Mux1
        elif RegDest == 0b010:
            output_Mux1.next = in3_Mux1
        elif RegDest == 0b011:
            output_Mux1.next = in4_Mux1
        elif RegDest == 0b100:
            output_Mux1.next = in5_Mux1
        else:
            output_Mux1.next = 0

    return behavior_Mux1

#Mux2 es de 2 a 1 y su selector es la variable definida como ALUsrc.
@block
def Mux2(ALUsrc, in1_Mux2, in2_Mux2, output_Mux2):
    
    #assert len(in1_Mux2) == len(in2_Mux2), "Ancho de entrada 1 y 2 distintos"
    #assert len(in2_Mux2) == len(output_Mux2), "Ancho de entrada 2 y salida distintos"
    
    @always_comb
    def behavior_Mux2():
        if ALUsrc == 0b0:
            output_Mux2.next = in1_Mux2
        else:
            output_Mux2.next = in2_Mux2

    return behavior_Mux2

#Mux3 es de 2 a 1 y su selector es la variable definida como Sel_Mux.
@block
def Mux3(Sel_Mux, in1_Mux3, in2_Mux3, output_Mux3):
    
    #assert len(in1_Mux3) == len(in2_Mux3), "Ancho de entrada 1 y 2 distintos"
    #assert len(in2_Mux3) == len(output_Mux3), "Ancho de entrada 2 y output distintos"
    
    @always_comb
    def behavior_Mux3():
        if Sel_Mux == 0b0:
            output_Mux3.next = in1_Mux3
        else:
            output_Mux3.next = in2_Mux3
            
    return behavior_Mux3

#Mux4 es de 2 a 1 y su selector es la variable definida como PCsrc.
@block
def Mux4(PCsrc, in1_Mux4, in2_Mux4, output_Mux4):
    
    #assert len(in1_Mux4) == len(in2_Mux4), "Ancho de entrada 1 y 2 distintos"
    #assert len(in2_Mux4) == len(output_Mux4), "Ancho de entrada 2 y output distintos"
    
    in1_concat = Signal(modbv(0)[31:])
    
    @always_comb
    def assing():
        in1_concat.next = in1_Mux4[32:1]
        
    @always_comb
    def behavior_Mux4():

        if PCsrc == 0b0:
            output_Mux4.next = concat(in1_concat, bool(0))
        else:
            output_Mux4.next = in2_Mux4

    return instances()


#Demux una entrada dos salidas
@block
def Demux(Sel_Demux, in_demux, out1_demux, out2_demux):
    
    #assert len(in_demux) == len(out1_demux), "ancho de entrada y salida 1 distintos"
    #assert len(in_demux) == len(out2_demux), "ancho de entrada y salida 2 distintos"
    
    @always_comb
    def behavior_Demux():
        out1_demux.next = 0
        out2_demux.next = 0
        if Sel_Demux == 0:
            out1_demux.next = in_demux
        else:
            out2_demux.next = in_demux
            
    return instances()

"""
Aclaratoria if __name__ == '__main__' esta indicando que si el archivo no es importado se ejecutara lo que esta dentro de la condicion
if, estas ultimas lineas son para la sintetizacion del codigo a verilog. Tomen en cuenta que si estan haciendo test del codigo no
es necesario cambiar nada solo importar este archivo y la condicion if __name__ == '__main__' nunca se cumplira por lo que solo sirve 
para corroborar que el codigo es sintetizable.
"""
if __name__ == '__main__':

    def convert_Mux1(hdl):

        # Inicialización de las funciones.
        RegDest = Signal(modbv(0)[4:0])
        in1_Mux1 = Signal(modbv(0)[32:0])
        in2_Mux1 = Signal(modbv(0)[32:0])
        in3_Mux1 = Signal(modbv(0)[32:0])
        in4_Mux1 = Signal(modbv(0)[32:0])
        in5_Mux1 = Signal(modbv(0)[32:0])
        output_Mux1 = Signal(modbv(0)[32:0])

        convertMux1 = Mux1(RegDest, in1_Mux1, in2_Mux1, in3_Mux1, in4_Mux1, in5_Mux1, output_Mux1)
        convertMux1.convert(hdl=hdl)

    def convert_Mux2(hdl):

        # Inicialización de las funciones.
        ALUsrc = Signal(modbv(0)[1:0])
        in1_Mux2 = Signal(modbv(0)[32:0])
        in2_Mux2 = Signal(modbv(0)[32:0])
        output_Mux2 = Signal(modbv(0)[32:0])

        convertMux2 = Mux2(ALUsrc, in1_Mux2, in2_Mux2, output_Mux2)
        convertMux2.convert(hdl=hdl)

    def convert_Mux3(hdl):

        # Inicialización de las funciones.
        Sel_Mux = Signal(modbv(0)[1:0])
        in1_Mux3 = Signal(modbv(0)[32:0])
        in2_Mux3 = Signal(modbv(0)[32:0])
        output_Mux3 = Signal(modbv(0)[32:0])

        convertMux3 = Mux3(Sel_Mux, in1_Mux3, in2_Mux3, output_Mux3)
        convertMux3.convert(hdl=hdl)

    def convert_Mux4(hdl):

        # Inicialización de las funciones.
        PCsrc = Signal(modbv(0)[1:0])
        in1_Mux4 = Signal(modbv(0)[32:0])
        in2_Mux4 = Signal(modbv(0)[32:0])
        output_Mux4 = Signal(modbv(0)[32:0])

        convertMux4 = Mux4(PCsrc, in1_Mux4, in2_Mux4, output_Mux4)
        convertMux4.convert(hdl=hdl)

    def convert_Demux(hdl):

        # Inicialización de las funciones.
        Sel_Demux = Signal(modbv(0)[1:])
        in_demux = Signal(modbv(0)[32:0])
        out1_demux= Signal(modbv(0)[32:0])
        out2_demux = Signal(modbv(0)[32:0])

        convert_Demux = Demux(Sel_Demux, in_demux, out1_demux, out2_demux)
        convert_Demux.convert(hdl=hdl)

    convert_Mux1(hdl='verilog')
    convert_Mux2(hdl='verilog')
    convert_Mux3(hdl='verilog')
    convert_Mux4(hdl='verilog')
    convert_Demux(hdl='verilog')
