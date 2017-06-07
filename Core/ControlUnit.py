#!/usr/bin/env python

from myhdl import *

class C_OPcode:
    """
    Tipos de operaciones
    """
    R_type = 0b0110011
    I_type = 0b0010011
    I_type_JALR = 0b1100111  # se usa para la funcion JALR junto funct3 = 0, es decir funct3 = 000 o ADDI
    I_type_LOAD = 0b0000011  # usadas para instrucciones de carga
    S_type = 0b0100011
    SB_type = 0b1100011
    # las instrucciones U_type tienen dos opcode
    U_type_LUI = 0b0110111
    U_type_AUIPC = 0b0010111
    # para la instruccion JAL
    UJ_type = 0b1101111


class C_funct3:
    """
    funciones 3 (funct3)
    """
#instrucciones de tipo R
    ADD = 0b000     
    SLT = 0b010
    SLTU = 0b011
    AND = 0b111
    OR = 0b110
    XOR = 0b100
    SLL = 0b001
    SRL = 0b101
    SUB = 0b000
    SRA = 0b101
#instrucciones de tipo I
    ADDI = 0b000    
    SLTI = 0b010
    SLTIU = 0b011
    ANDI = 0b111
    ORI = 0b110
    XORI = 0b100
    SLLI = 0b001
    SRLI = 0b101
    SRAI = 0b101
#intrucciones de tipo I para load
    LB = 0b000  
    LH = 0b001
    LW = 0b010
    LBU = 0b100
    LHU = 0b101
#instrucciones de tipo s (store)
    SB = 0b000      
    SH = 0b001
    SW = 0b010
# instrucciones de tipo SB
    BEQ = 0b000     
    BNE = 0b001
    BLT = 0b100
    BGE = 0b101
    BLTU = 0b110
    BGEU = 0b111


class C_funct7:
    """
    funciones 7 (funct7)
    """
    type1 = 0b0000000 # para R_type en ADD/SLT/SLTU/AND/OR/XOR/SLL/SRL y para imm[11:5] usado en I_type para SLLI/SRLI
    type2 = 0b0100000 # para R_type en SUB/SRA y para imm[11:5] usado en I_type para SRAI


class C_ALUop:
    """
    Operaciones de la ALU
    """
    OP_ADD = 0
    OP_SUB  = 1
    OP_XOR  = 2
    OP_OR   = 3
    OP_AND  = 4
    OP_SRL  = 5
    OP_SLL  = 6
    OP_SRA  = 7
    OP_SLT  = 8
    OP_SLTU = 9
    OP_BEQ = 10 #Si r1d y r2d son iguales, flag = 1
    # OJO! BNE está como BNQ en la ALU
    OP_BNE = 11 #Si r1d y r2d son distintas, flag = 1
    OP_BLT = 12 #Si r1d es menor a r2d, flag = 1 (signed)
    OP_BLTU = 13 #Si r1d es menor a r2d, flag = 1 (unsigned)
    OP_BGE = 14 #Si r1d es mayor o igual a r2d, flag = 1 (signed)
    OP_BGEU = 15 #Si r1d es mayor o igual a r2d, flag = 1 (unsigned)

@block
def ControlUnit (OPcode, funct7, funct3, branch, RegWrite, RegDest, ALUsrc, ALUop, DWidth, PCsrc, Sel_Mux):
    """
    Entradas: OPcode, funct7, funct3, branch.
    Salidas: RegWrite, RegDest, ALUsrc, ALUop, DWidth, PCsrc, Sel_Mux, PC_next.
    
    Longitudes de las salidas:
    RegWrite, 1 bit.
    RegDest, 3 bits.
    ALUsrc, 1 bits.
    ALUop, 4 bits.
    DWidth, 3 bits.
    PCsrc, 1 bits.
    Sel_Mux, 1 bit.
    """
    assert len(OPcode) == 7, "OPcode no es de 7 bits"
    assert len(funct7) == 7, "funct7 no es de 7 bits"
    assert len(funct3) == 3, "funct3 no es de 3 bits"
    assert len(branch) == 1, "branch no es de 1 bit"

    @always_comb
    def behavior():
        """
        Para el set de instrucciones de tipo R es necesaria la funct3 y funct7, pero para el funcionamiento del codigo 
        no es estrictamente necesario. Por esa razón la mayoria de los condiciones dentro de if OPcode == C_OPcode.R_type 
        evaluan ambas codiciones.
        Para todas las operaciones tipo R ALUsrc.next = 0b0 y DWidth no es utilizado.
        """
        RegWrite.next = 0b0
        # OJO! por Default elige salida de ALU
        RegDest.next = 0b100
        # OJO! por Default elige salida del Register File
        ALUsrc.next = 0b0
        #OJO! por Default elige operacion suma en la ALU
        ALUop.next = 0b0000
        # OJO! 
        DWidth.next = 0b101
        # OJO! por default elige PC + 4
        PCsrc.next = 0b1
        Sel_Mux.next = 0b0
    
        if OPcode == C_OPcode.R_type:

            RegWrite.next = 0b1
            RegDest.next = 0b100
            ALUsrc.next = 0b0
            PCsrc.next = 0b1
            Sel_Mux.next= 0b0

            if funct3 == C_funct3.ADD and funct7 == C_funct7.type1:
                ALUop.next = C_ALUop.OP_ADD
            elif funct3 == C_funct3.SUB and funct7 == C_funct7.type2:
                ALUop.next = C_ALUop.OP_SUB
            elif funct3 == C_funct3.SLL and funct7 == C_funct7.type1:
                ALUop.next = C_ALUop.OP_SLL
            elif funct3 == C_funct3.SLT and funct7 == C_funct7.type1:
                ALUop.next = C_ALUop.OP_SLT
            elif funct3 == C_funct3.SLTU and funct7 == C_funct7.type1:
                ALUop.next = C_ALUop.OP_SLTU
            elif funct3 == C_funct3.XOR and funct7 == C_funct7.type1:
                ALUop.next = C_ALUop.OP_XOR
            elif funct3 == C_funct3.SRL and funct7 == C_funct7.type1:
                ALUop.next = C_ALUop.OP_SRL
            elif funct3 == C_funct3.SRA and funct7 == C_funct7.type2:
                ALUop.next = C_ALUop.OP_SRA
            elif funct3 == C_funct3.OR and funct7 == C_funct7.type1:
                ALUop.next = C_ALUop.OP_OR
            elif funct3 == C_funct3.AND and funct7 == C_funct7.type1:
                ALUop.next = C_ALUop.OP_AND
            else:
                ALUop.next = C_ALUop.OP_ADD

        """
        El set de instrucciones de tipo I posee instrucciones que usan un immediato de 12 bits (imm[11:0]) 
        y unos que usan dos immediatos uno de 5 bits (imm[4:0] = shamt = shift amount), otro de 7 bits (imm[11:5]) que 
        indica si usar SLLI/SRLI o SRAI
        DWidth es irrelevante.
        """

        if OPcode == C_OPcode.I_type:

            RegWrite.next = 0b1
            RegDest.next = 0b100
            PCsrc.next = 0b1
            ALUsrc.next = 0b1
            Sel_Mux.next = 0b0
            #DWidth.next = 0bxxx

            if funct3 == C_funct3.ADDI:
                ALUop.next = C_ALUop.OP_ADD
            elif funct3 == C_funct3.SLTI:               
                ALUop.next = C_ALUop.OP_SLT
            elif funct3 == C_funct3.SLTIU:
                ALUop.next = C_ALUop.OP_SLTU
            elif funct3 == C_funct3.XORI:
                ALUop.next = C_ALUop.OP_XOR
            elif funct3 == C_funct3.ORI:
                ALUop.next = C_ALUop.OP_OR
            elif funct3 == C_funct3.ANDI:
                ALUop.next = C_ALUop.OP_AND
            elif funct3 == C_funct3.SLLI and funct7 == C_funct7.type1:
                ALUop.next = C_ALUop.OP_SLL
            elif funct3 == C_funct3.SRLI and funct7 == C_funct7.type1:
                ALUop.next = C_ALUop.OP_SRL
            elif funct3 == C_funct3.SRAI and funct7 == C_funct7.type2:
                ALUop.next = C_ALUop.OP_SRA
            else:
                ALUop.next = C_ALUop.OP_ADD
                
        """
        En la instruccion JALR que es de tipo I se usa la operacion de ADD para sumar el registro de direccion rs1 con imm[11:0] de 12 bits, y colocar el 
        LSB en 0, esto ultimo se realiza colocando el cable a tierra en el bus de datos, para no agregar una operacion mas a la ALU.
        Para este tipo de instruccion no importa el valor que tenga la variable Dwidth, Sel_Mux.
        """

        if OPcode == C_OPcode.I_type_JALR and funct3 == 0b000:
        
            RegWrite.next = 0b1
            RegDest.next = 0b000
            ALUsrc.next = 0b1
            ALUop.next = C_ALUop.OP_ADD
            #DWidth.next = 0bxxx
            PCsrc.next = 0b0
            #Sel_Mux.next = 0bx
        
        """
        Para las instrucciones de carga (I_type_LOAD) se obtendra la dirección del dato a cargar sumando el inmediato (extendido con signo) con el registro rs1
        y se recibe de la memoria un BYTE, HALFWORD o WORD dependiendo de la función el cual se extiende con signo o sin signo
        """

        if OPcode == C_OPcode.I_type_LOAD:

            RegWrite.next = 0b1
            RegDest.next = 0b011
            ALUsrc.next = 0b1
            ALUop.next = C_ALUop.OP_ADD
            PCsrc.next = 0b1
            Sel_Mux.next = 0b0

            if funct3 == C_funct3.LB:
                DWidth.next = 0b000
            elif funct3 == C_funct3.LH:
                DWidth.next = 0b001
            elif funct3 == C_funct3.LW:
                DWidth.next = 0b010
            elif funct3 == C_funct3.LBU:
                DWidth.next = 0b011
            elif funct3 == C_funct3.LHU:
                DWidth.next = 0b100
            else:
                DWidth.next = 0b101 # No hace nada en este modulo

        """
        Para las instrucciones de tipo S (store) solo se ultiliza la escritura en la memoria, por lo que deshabilitamos RegWrite y las salidas
        RegDest/ALUsrc/ALUop/Ext_E
        """

        if OPcode == C_OPcode.S_type:

            RegWrite.next = 0b0
            RegDest.next = 0b011
            ALUsrc.next = 0b1
            ALUop.next = C_ALUop.OP_ADD
            DWidth.next = 0b000
            PCsrc.next = 0b1
            Sel_Mux.next = 0b0
            
            if funct3 == C_funct3.SB:
                DWidth.next = 0b000
            elif funct3 == C_funct3.SH:
                DWidth.next = 0b001
            elif funct3 == C_funct3.SW:
                DWidth.next = 0b010
            else:
                DWidth.next = 0b101

        """
        Para la instruccion branch, tipo SB, se carga un inmediato para sumarlo a la direccion actual del PC, y este sera la siguiente instruccion siempre y cuando se cumpla
        la condicion del branch (funct3) que sale de una comparacion exitosa de la ALU (flag branch). 
        No son necesarios RegDest, Ext_E y DWidth. Deshabilitamos RegWrite. La operacion de la ALU dependera del funct3 y
        Pcsrc dependera de si se cumple el branch o no.
        """

        if OPcode == C_OPcode.SB_type:

            RegWrite.next = 0b0
            #RegDest.next = 0bxxx
            ALUsrc.next = 0b0
            #DWidth.next = 0bxxx
            PCsrc.next = 0b1
            Sel_Mux.next = 0b1
            
            if funct3 == C_funct3.BEQ:
                ALUop.next = C_ALUop.OP_BEQ
            elif funct3 == C_funct3.BNE:
                ALUop.next = C_ALUop.OP_BNE
            elif funct3 == C_funct3.BLT:
                ALUop.next = C_ALUop.OP_BLT
            elif funct3 == C_funct3.BGE:
                ALUop.next = C_ALUop.OP_BGE
            elif funct3 == C_funct3.BLTU:
                ALUop.next = C_ALUop.OP_BLTU
            elif funct3 == C_funct3.BGEU:
                ALUop.next = C_ALUop.OP_BGEU
            else:
                ALUop.next = C_ALUop.OP_ADD
            
            if branch == 0b1:
                Sel_Mux.next = 0b1
            else:
                Sel_Mux.next = 0b0

        """
        Para la instruccion LUI, tipo U, se almacena un inmediato rellanado con 0's (Fill) en el registro deseado. Debemos habilitar la escritura en los registros (RegWrite=1), deshabilitar
        la escritura y lectura de datos en la memoria RAM ya que no son necesarios, la siguiente instruccion de la PC es PC + 4 (PCsrc = 00) y seleccionamos la entrada
        del fill a la escritura de los registros (RegDest=010). No son necesarrios ALUsrc, Ext_E ni DWidth.
        """
        if OPcode == C_OPcode.U_type_LUI:

            RegWrite.next = 0b1
            RegDest.next = 0b010
            #ALUsrc.next = 0bx
            #ALUop.next = 0bxxxx
            #DWidth.next = 0bxxx
            PCsrc.next = 0b1
            Sel_Mux.next = 0b0

        """
        Para la instruccion AUIPC, tipo U, tomamos un inmediato de 20 bits de la instruccion, rellenamos con 0's los bits menos significativos para completar los 32 bits (Fill), se lo sumamos a la direccion actual de la PC y
        lo almacenamos en el registro deseado. Para esto, habilitamos la escritura de los registros, hacemos que la entrada del registro sea la sumatoria del FIll con la direccion de PC (RegDest=001).
        La siguiente instruccion del PC es PC + 4, entonces PCsrc = 00 y deshabilitamos la escritura y lectura de datos de la memoria RAM ya que no son necesarios.
        """
        if OPcode == C_OPcode.U_type_AUIPC:

            RegWrite.next = 0b1
            RegDest.next = 0b001
            #ALUsrc.next = 0bx
            #ALUop.next = 0bxxxx
            #DWidth.next = 0bxxx
            PCsrc.next = 0b1
            Sel_Mux.next = 0b0

        """
        Para la instruccion JAL, tipo UJ, guardaremos la instruccion PC + 4 en el registro deseado. Ademas, tomamos un inmediato de la instruccion, la extendemos 
        y se la sumamos a la direccion actual del PC. Este resultado sera la siguiente instruccion del PC. Para esto, habilitamos la escritura de los registros, 
        hacemos que la entrada del registro sea PC + 4 (RegDest=000) y para indicar la siguiente instruccion del PC hacemos PCsrc = 1. Deshabilitamos la escritura
        y lectura de datos de la memoria RAM ya que no son necesarios.
        ALUsrc, ALUop, DWidth no son necesarios.
        """
        if OPcode == C_OPcode.UJ_type:

            RegWrite.next = 0b1
            RegDest.next = 0b000
            #ALUsrc.next = 0bx
            #ALUop.next = 0bxxxx
            #DWidth.next = 0bxxx
            PCsrc.next = 0b1
            Sel_Mux.next = 0b1
            
    return behavior

if __name__ == '__main__':

    # Inicialización de las señales.
    OPcode = Signal(modbv(0)[7:])
    funct7 = Signal(modbv(0)[7:])
    funct3 = Signal(modbv(0)[3:])
    branch = Signal(modbv(0)[1:]) 
    RegWrite = Signal(modbv(0)[1:]) 
    RegDest = Signal(modbv(0)[3:])
    ALUsrc = Signal(modbv(0)[1:])
    ALUop = Signal(modbv(0)[4:])
    DWidth = Signal(modbv(0)[3:])
    PCsrc = Signal(modbv(0)[1:])
    Sel_Mux = Signal(modbv(0)[1:])

    CU_instance = ControlUnit(OPcode, funct7, funct3, branch, RegWrite, RegDest, ALUsrc, ALUop, DWidth, PCsrc, Sel_Mux)

    CU_instance.convert(hdl='Verilog')
