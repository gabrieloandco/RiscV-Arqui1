from FSM import *
from myhdl import *
import random

@block
def tbFSM():
    # Entradas
    OPcode  = Signal(modbv(35)[8:0]) #si se coloca 35 realiza store, 3 load y otra cosa fecth/decode.
    RAMdone = Signal(modbv(0)[1:0])
    #EstadoPresente = Signal(modbv(0)[2:0])
    #EstadoPresente = Signal(Estado.Fetch)
    clk = Signal(bool(0))
    reset = ResetSignal(0, active = 1, async=True)
    #EstadoPresente = Signal(modbv(0)[2:0])
    #SiguienteEstado = Signal(modbv(0)[2:0])

    # Salidas
    RAMwrite  = Signal(modbv(0)[1:0])
    RAMread   = Signal(modbv(0)[1:0])
    Demux_Sel = Signal(modbv(0)[1:0])
    Mux5_Sel  = Signal(modbv(0)[1:0])
    MBR_go    = Signal(modbv(0)[1:0])
    RegOk     = Signal(modbv(0)[1:0])
    ok_pc     = Signal(modbv(0)[1:0])

    dut = FSM(clk, reset, OPcode, RAMdone, RAMwrite, RAMread, Demux_Sel, Mux5_Sel, MBR_go, RegOk, ok_pc)

    
    wait = delay(40)
    
    
    @always(delay(10))
    def clkgen():
        clk.next = not clk
    
    @instance
    def stim():
        RAMdone.next = 0
        #OPcode.next = 0b0000011
        
        yield wait

        RAMdone.next = 1
        yield delay(10)

        RAMdone.next = 0
        #OPcode.next = 0b0100011
        yield wait

        RAMdone.next = 1
        yield delay(10)

        RAMdone.next = 0
        #OPcode.next = random.randrange(0, 2**7)
        yield delay(60)

        RAMdone.next = 1
        yield delay(10)

        RAMdone.next = 0
        #OPcode = random.randrange(0, 2**7)
        yield delay(60)

        RAMdone.next = 1
        yield wait

        

    return dut, stim, clkgen


test = tbFSM()
test.config_sim(trace=True)
test.run_sim(1000)
