from ControlUnit import *
from myhdl import *

@block
def testControlUnit():

	#Entradas 
 
    OPcode = Signal(modbv(0)[7:0])
    funct7 = Signal(modbv(0)[7:0]) 
    funct3 = Signal(modbv(0)[3:0])
    branch = Signal(modbv(0)[1:0])
    x = Signal(modbv(0)[1:0])

	#Salidas 

    RegWrite = Signal(modbv(0)[1:]) 
    RegDest = Signal(modbv(0)[3:])
    ALUsrc = Signal(modbv(0)[1:])
    ALUop = Signal(modbv(0)[4:])
    DWidth = Signal(modbv(0)[3:])
    PCsrc = Signal(modbv(0)[1:])
    Sel_Mux = Signal(modbv(0)[1:])

    dut = ControlUnit(OPcode, funct7, funct3, branch, RegWrite, RegDest, ALUsrc, ALUop, DWidth, PCsrc, Sel_Mux)
    cont = Signal(modbv(0)[4:])

    interv = delay(1)
    
    @always(interv)
    def stim():
        
        x.next = 0
        if cont == 0:

            OPcode.next = 0b0110011          #TIPO R
            for i in range(10):    

                    
                if i == 0:
                    funct7.next = 0b0000000                
                    funct3.next = 0b000       #ADD
                elif i == 1:
                    funct7.next = 0b0000000
                    funct3.next = 0b010       #SLT
                elif i == 2:
                    funct7.next = 0b0000000                
                    funct3.next = 0b011       #SLTU
                elif i == 3:
                    funct7.next = 0b0000000                
                    funct3.next = 0b111       #AND
                elif i == 4:
                    funct7.next = 0b0000000                
                    funct3.next = 0b110       #OR
                elif i == 5:
                    funct7.next = 0b0000000                
                    funct3.next = 0b100       #XOR
                elif i == 6:
                    funct7.next = 0b0000000                
                    funct3.next = 0b001       #SLL
                elif i == 7:
                    funct7.next = 0b0000000                
                    funct3.next = 0b101       #SRL 
                elif i == 8:
                    funct7.next = 0b0100000
                    funct3.next = 0b000       #SUB 
                elif i == 9:
                    funct7.next = 0b0100000                
                    funct3.next = 0b101       #SRA
                
                                                
        elif cont==1:   
             
            OPcode.next = 0b0010011          #TIPO I 
            for i in range(9):    
                funct7.next = 0b0000000
                 
                if i == 0:               
                    funct3.next = 0b000       #ADDI
                elif i == 1:
                    funct3.next = 0b010       #SLTI
                elif i == 2:               
                    funct3.next = 0b011       #SLTUI
                elif i == 3:               
                    funct3.next = 0b111       #ANDI
                elif i == 4:               
                    funct3.next = 0b110       #ORI
                elif i == 5:                
                    funct3.next = 0b100       #XORI
                elif i == 6:               
                    funct3.next = 0b001       #SLLI
                elif i == 7:                
                    funct3.next = 0b101       #SRLI
                elif i == 8:
                    funct3.next = 0b101       #SRA1
        elif cont==2:            
                                              
            OPcode.next = 0b1100111              #TIPO I JAR
            funct3.next == 0b000

	        
        elif cont==3:

            OPcode.next = 0b0000011          #TIPO I para load
            for i in range(5):    
                    
                    
                if i == 0:
                   funct3.next  = 0b000      #LB      
                elif i == 1:
                   funct3.next  = 0b001      #LH
                elif i == 2:
                   funct3.next  = 0b010      #LW          
                elif i == 3:
                   funct3.next  = 0b100      #LBU          
                elif i == 4:
                   funct3.next = 0b101       #LHU        
                else:
                   funct3.next  = 0b111      

        elif cont==4:
        
            OPcode.next = 0b0100011          #TIPO S
            for i in range(3):    
                    
                    
                if i == 0:
                    funct3.next  = 0b000      #SB      
                elif i == 1:
                    funct3.next  = 0b001      #SH
                elif i == 2:
                    funct3.next  = 0b010      #SW          
                else:
                    funct3.next  = 0b111      
            
        elif cont==5:

            OPcode.next = 0b1100011          #TIPO SB
            for i in range(6): 
                    
                    
                if i == 0:
                    funct3.next  = 0b000      #BEQ      
                elif i == 1:
                    funct3.next  = 0b001      #BNE
                elif i == 2:
                    funct3.next  = 0b100      #BLT         
                elif i == 3:
                    funct3.next  = 0b101      #BGE 
                elif i == 4:
                    funct3.next  = 0b110      #BLTU    
                elif i == 5:
                    funct3.next  = 0b111      #BGEU 
                else:
                    funct3.next  = 0b111       

                if x == 0:                  
                    branch.next = 0b1            #Sel.mux=1
                    x.next=1
                else:
                    branch.next = 0b0            #Sel.mux=0
                    x.next=0

        elif cont==6:
            
            OPcode.next = 0b0110111
            
        elif cont==7:

            OPcode.next = 0b0010111
            
        elif cont==8:

            OPcode.next = 0b1101111

        cont.next = cont.next + 1

    return dut, stim

test = testControlUnit()
test.config_sim(trace=True)
test.run_sim(1000)



