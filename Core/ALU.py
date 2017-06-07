"""
Fecha de subida:  1/10/16
Ultima fecha de edicion: 16/11/16
Ultimo en editar: Adrián H.
"""

from myhdl import *
#falta importar inA, inB, ALUop

@block
def ALU(inA,
        inB,
        ALUop,
        out,
        flag):
    """
        Unidad Logica Aritmetica del Procesador

        Lista de parametros:
        flag: bandera, va a control unit. Se activa si la salida es igual a cero        (1b)
        inA : entrada A. Proviene de los registros                                      (32b)
        inB : entrada B. Proviene de Mux 2                                              (32b)
        ALUOp  : selector de operaciones. Proviene de control unit                      (4b)
        out : salida, resultado de la operación                                         (32b)
    """
    ADD  = 0
    SUB  = 1
    XOR  = 2
    OR   = 3
    AND  = 4
    SRL  = 5
    SLL  = 6
    SRA  = 7
    SLT  = 8
    SLTU = 9
    BEQ  = 10
    BNQ  = 11
    BLT  = 12
    BLTU = 13
    BGE  = 14
    BGEU = 15
    
    """
        Asignación de la salida out:
        
        ADD : inA + inB
        SUB : inA - inB
        XOR : aplica XOR bit a bit entre inA e inB
        OR  : aplica OR bit a bit entre inA e inB
        AND : aplica AND bit a bit entre inA e inB
        SRL : desplaza los bits de inA, inB saltos a la derecha (sin signo)
        SLL : desplaza los bits de inA, inB saltos a la izquierda (sin signo)
        SRA : desplaza los bits de inA, inB saltos a la derecha (con signo)
        SLT : si inA >= inB, out = 0 (flag = 1), si inA < inB, out = 1 (flag = 0) (con signo)
        SLTU: si inA >= inB, out = 0 (flag = 1), si inA < inB, out = 1 (flag = 0) (sin signo)
        BEQ : si inA != inB, out = 0 (flag = 1), si inA = inB, out = 1 (flag = 0)
        BNQ : si inA = inB, out = 0 (flag = 1), si inA != inB, out = 1 (flag = 0)
        BLT : si inA < inB, out = 0 (flag = 1), si inA >= inB, out = 1 (flag = 0) (con signo)
        BLTU: si inA < inB, out = 0 (flag = 1), si inA >= inB, out = 1 (flag = 0) (sin signo)
        BGE : si inA >= inB, out = 0 (flag = 1), si inA < inB, out = 1 (flag = 0) (con signo)
        BGEU: si inA >= inB, out = 0 (flag = 1), si inA < inB, out = 1 (flag = 0) (sin signo)
    """
    @always_comb
    def output():
        flag.next = 0
        if   ALUop == ADD:  
            out.next = inA + inB
            if(inA + inB == 0):
            	flag.next = 1
        elif ALUop == SUB:
            out.next = inA - inB
            if (inA - inB == 0):
            	flag.next = 1
        elif ALUop == XOR:
            out.next = inA ^ inB
            if (inA ^ inB == 0):
            	flag.next = 1
        elif ALUop == OR:
            out.next = inA | inB
            if (inA | inB == 0):
            	flag.next = 1
        elif ALUop == AND:
            out.next = inA & inB
            if (inA & inB == 0):
            	flag.next = 1
        elif ALUop == SRL:
            out.next = inA >> inB [5:0]
            if (inA >> inB [5:0] == 0):
            	flag.next = 1
        elif ALUop == SLL:
            out.next = inA << inB [5:0]
            if (inA << inB [5:0] == 0):
            	flag.next = 1
        elif ALUop == SRA:
            out.next = inA.signed() >> inB[5:0]
            if (inA.signed() >> inB[5:0] == 0):
            	flag.next = 1
        elif ALUop == SLT:
            if (inA.signed() - inB.signed() < 0):
                out.next = modbv(1)[32:] 
            else:
                out.next = modbv(0)[32:]
                flag.next = 1
        elif ALUop == SLTU:
            if (inA -inB < 0):
                out.next = modbv(1)[32:]
            else:
                out.next = modbv(0)[32:]
                flag.next = 1
        elif ALUop == BEQ:
            if (inA == inB):
                out.next = modbv(1)[32:]
            else:
                out.next = modbv(0)[32:]
                flag.next = 1
        elif ALUop == BNQ:
            if (inA != inB):
                out.next = modbv(1)[32:]
            else:
                out.next = modbv(0)[32:]
                flag.next = 1
        elif ALUop == BLT:
            if (inA.signed() - inB.signed() < 0):
                out.next = modbv(0)[32:]
                flag.next = 1
            else:
                out.next = modbv(1)[32:]
        elif ALUop == BLTU:
            if (inA - inB < 0):
                out.next = modbv(0)[32:]
                flag.next = 1
            else:
                out.next = modbv(1)[32:]
        elif ALUop == BGE:
            if (inA.signed() - inB.signed() < 0):
                out.next = modbv(1)[32:]
            else:
                out.next = modbv(0)[32:]
                flag.next = 1
        elif ALUop == BGEU:
            if (inA - inB < 0):
                out.next = modbv(1)[32:]
            else:
                out.next = modbv(0)[32:]
                flag.next = 1
    return output

if __name__ == '__main__':
    def convert_ALU(hdl):
        inA=Signal(modbv(0)[32:])
        inB=Signal(modbv(0)[32:])
        ALUop=Signal(modbv(0)[4:])
        out=Signal(modbv(0)[32:])
        flag=Signal(modbv(0)[1:])
        con = ALU(inA,inB,ALUop,out,flag)
        con.convert(hdl=hdl)
    convert_ALU(hdl = 'verilog')

"""
         Cambios (8/10)
               Cambiados nombres de varibles por las de esquemático. inA->r1d, inB->r2d, op->ALUop 
               Agregadas operaciones BEQ, BNQ, BLT, BLTU, BGE, BGEU
               
               (10/10)
               La flag zero da un pulso cuando out = 0 y al siguiente ciclo del reloj, se apaga.
               Arreglada declaración de variables de salida
                
               (11/10)
               Nueva implementación de la flag zero
               
               (19/10)
               Cambio de nombres. rd1 -> inA; rd2 -> inB; zero -> flag
               
               (27/10)
               Cambios para que la conversión a verilog fuera exitosa:
               - Se eliminaron los modbv ( _<operacion>), por lo que los elif comparan ALUop con enteros
               - Se asigna el valor de la flag zero dentro de cada elif, no despues de ellos
               
               (15/11)
               - Arreglada la lógica de BEQ y BNQ"""
