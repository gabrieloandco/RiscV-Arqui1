from ALU import *
from myhdl import *
import random

@block
def testALU():

    #Entradas
    inA = Signal(modbv(0)[32:])
    inB = Signal(modbv(0)[32:])
    ALUop = Signal(modbv(0)[4:])

    #Salidas
    out = Signal(modbv(0)[32:])
    flag =  Signal(modbv(0)[1:])


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


    dut = ALU(inA, inB, ALUop, out, flag)

    interv = delay(1)

    @always(interv)
    def stim():

        inA.next = random.randint(0,(2**32))
        inB.next = random.randint(0,(2**32))
        
        if ALUop == ADD:
            assert out == modbv(inA + inB)[32:], "Error ADD, inA:{0},inB:{1}, out:{2}".format(inA, inB, out)
            if out == 0: 
                assert flag == 1, "Error flag ADD, inA:{0},inB:{1}, out:{2}, flag:{3}".format(inA, inB, out, flag)
        elif ALUop == SUB:
            assert out == modbv(inA - inB)[32:], "Error SUB, inA:{0},inB:{1}, out:{2}".format(inA, inB, out)
            if out == 0: 
                assert flag == 1, "Error flag SUB, inA:{0},inB:{1}, out:{2}, flag:{3}".format(inA, inB, out, flag)
        elif ALUop == XOR: 
            assert out == ( inA ^ inB ), "Error XOR, inA:{0},inB:{1}, out:{2}".format(inA, inB, out)
            if out == 0: 
                assert flag == 1, "Error flag XOR, inA:{0},inB:{1}, out:{2}, flag:{3}".format(inA, inB, out, flag)
        elif ALUop == OR:
            assert out == ( inA | inB ), "Error OR, inA:{0},inB:{1}, out:{2}".format(inA, inB, out)
            if out == 0: 
                assert flag == 1, "Error flag OR, inA:{0},inB:{1}, out:{2}, flag:{3}".format(inA, inB, out, flag)
        elif ALUop == AND: 
            assert out == ( inA & inB ), "Error AND, inA:{0},inB:{1}, out:{2}".format(inA, inB, out)
            if out == 0: 
                assert flag == 1, "Error flag AND, inA:{0},inB:{1}, out:{2}, flag:{3}".format(inA, inB, out, flag)
        elif ALUop == SRL:
            assert out == modbv( inA >> inB[5:0] )[32:], "Error SRL, inA:{0},inB:{1}, out:{2}".format(inA, inB, out)
            if out == 0: 
                assert flag == 1, "Error flag SRL, inA:{0},inB:{1}, out:{2}, flag:{3}".format(inA, inB, out, flag)
        elif ALUop == SLL:
            assert out == modbv(inA.signed() << inB[5:0])[32:], "Error SLL, inA:{0},inB:{1}, out:{2}".format(inA, inB, out)
            if out == 0: 
                assert flag == 1, "Error flag SLL, inA:{0},inB:{1}, out:{2}, flag:{3}".format(inA, inB, out, flag)
        elif ALUop == SRA:
            assert out == modbv(inA.signed() >> inB[5:0])[32:], "Error SRA, inA:{0},inB:{1}, out:{2}".format(inA, inB, out)
            if out == 0: 
                assert flag == 1, "Error flag SRA, inA:{0},inB:{1}, out:{2}, flag:{3}".format(inA, inB, out, flag)
        elif ALUop == SLT:
            assert out == ( inA.signed() < inB.signed() ), "Error SLT, inA:{0},inB:{1}, out:{2}".format(inA, inB, out)
            if out == 0: 
                assert flag == 1, "Error flag SLT, inA:{0},inB:{1}, out:{2}, flag:{3}".format(inA, inB, out, flag)
        elif ALUop == SLTU:
            assert out == (inA < inB ), "Error SLTU, inA:{0},inB:{1}, out:{2}".format(inA, inB, out) 
            if out == 0: 
                assert flag == 1, "Error flag SLTU, inA:{0},inB:{1}, out:{2}, flag:{3}".format(inA, inB, out, flag)
        elif ALUop == BEQ:
            assert out == (inA == inB) , "Error BEQ, inA:{0},inB:{1}, out:{2}".format(inA, inB, out)
            if out == 0: 
                assert flag == 1, "Error flag BEQ, inA:{0},inB:{1}, out:{2}, flag:{3}".format(inA, inB, out, flag)
        elif ALUop == BNQ:
            assert out == ( inA != inB ), "Error BNQ, inA:{0},inB:{1}, out:{2}".format(inA, inB, out)
            if out == 0: 
                assert flag == 1, "Error flag BNQ, inA:{0},inB:{1}, out:{2}, flag:{3}".format(inA, inB, out, flag)
        elif ALUop == BLT:
            assert out == ( inA.signed() < inB.signed() ), "Error BLT, inA:{0},inB:{1}, out:{2}".format(inA, inB, out)
            if out == 0: 
                assert flag == 1, "Error flag BLT, inA:{0},inB:{1}, out:{2}, flag:{3}".format(inA, inB, out, flag)
        elif ALUop == BLTU:
            assert out == (inA - inB < 0) , "Error BLTU, inA:{0},inB:{1}, out:{2}".format(inA, inB, out)
            if out == 0: 
                assert flag == 1, "Error flag BLTU, inA:{0},inB:{1}, out:{2}, flag:{3}".format(inA, inB, out, flag)
        elif ALUop == BGE:
            assert out == ( inA.signed() < inB.signed() ), "Error BGE, inA:{0},inB:{1}, out:{2}".format(inA, inB, out)
            if out == 0: 
                assert flag == 1, "Error flag BGE, inA:{0},inB:{1}, out:{2}, flag:{3}".format(inA, inB, out, flag)
        elif ALUop == BGEU:
            assert out == ( inA < inB ), "Error BGEU, inA:{0},inB:{1}, out:{2}".format(inA, inB, out)
            if out == 0: 
                assert flag == 1, "Error flag BGEU, inA:{0},inB:{1}, out:{2}, flag:{3}".format(inA, inB, out, flag)
        elif ALUop >= 17:
            assert ALUop >= 17, "ERROR: Operacion no definida"
            

        ALUop.next = ALUop.next + 1 



    return dut, stim

test = testALU()
test.config_sim(trace=True)
test.run_sim(1000)
