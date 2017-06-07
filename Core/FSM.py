#!/usr/bin/env python

from myhdl import *

class opcode:
    Load = 0b0000011
    Store = 0b0100011

class Estado:
    Fetch = 0b000
    Decode = 0b001
    Load = 0b010
    Store = 0b011
    LoadWait = 0b100

@block
def FSM (clk, reset, OPcode, RAMdone, RAMwrite, RAMread, Demux_Sel, Mux5_Sel, MBR_go, RegOk, ok_pc):

    """
    Entradas: OPcode de 7 bits.
              RAMdone de 1 bit.
              clk de 1 bit
              reset de 1 bit
    Salidas: RAMwrite  de 1 bit.
             RAMread de 1 bit.
             Demux_Sel de 1 bit.
             Mux5_Sel de 1 bit.
             MBR_go de 1 bit.
             RegOk de 1 bit.
             ok_pc de 1 bit
    """
    EstadoPresente = Signal(modbv(0)[3:0])
    
    @always_seq(clk.posedge, reset = reset)
    def Logic():
        if reset == 1:
            RAMwrite.next = 0b0
            RAMread.next = 0b0
            Demux_Sel.next = 0b0
            Mux5_Sel.next = 0b0
            MBR_go.next = 0b0
            RegOk.next = 0b0
            ok_pc.next = 1
            EstadoPresente.next = Estado.Fetch
        
        else:
           
            if EstadoPresente == Estado.Fetch:
                RAMwrite.next = 0b0
                RAMread.next = 0b1
                Demux_Sel.next = 0b0
                Mux5_Sel.next = 0b0
                MBR_go.next = 0b0
                RegOk.next = 0b0
                ok_pc.next = 0b0
                if RAMdone == 1:
                    MBR_go.next = 1
                    EstadoPresente.next = Estado.Decode

            elif EstadoPresente == Estado.Decode:
                RAMwrite.next = 0b0
                RAMread.next = 0b0
                Demux_Sel.next = 0b0
                Mux5_Sel.next = 0b0
                MBR_go.next = 0b0
                RegOk.next = 0b0
                ok_pc.next = 0b0
                if OPcode != opcode.Load and OPcode != opcode.Store:
                    ok_pc.next = 1
                    RegOk.next = 1
                    EstadoPresente.next = Estado.Fetch

                elif OPcode == opcode.Load:
                    EstadoPresente.next = Estado.Load

                elif OPcode == opcode.Store:
                    EstadoPresente.next = Estado.Store

            elif EstadoPresente == Estado.Load:
                RAMwrite.next = 0b1
                RAMread.next = 0b1
                Demux_Sel.next = 0b1
                Mux5_Sel.next = 0b1
                MBR_go.next = 0b0
                RegOk.next = 0b0
                ok_pc.next = 0b0
                if RAMdone == 1:
                    Mux5_Sel.next = 0b0
                    Demux_Sel.next = 0b0
                    RegOk.next = 1
                    EstadoPresente.next = Estado.LoadWait

            elif EstadoPresente == Estado.Store:
                RAMwrite.next = 0b1
                RAMread.next = 0b1
                Demux_Sel.next = 0b0
                Mux5_Sel.next = 0b1
                MBR_go.next = 0b0
                RegOk.next = 0b0
                ok_pc.next = 0
                if RAMdone == 1:
                    ok_pc.next = 1
                    EstadoPresente.next = Estado.Fetch

            elif EstadoPresente == Estado.LoadWait:
                RAMwrite.next = 0b1
                RAMread.next = 0b1
                Demux_Sel.next = 0b0
                Mux5_Sel.next = 0b0
                MBR_go.next = 0b0
                RegOk.next = 0b0
                ok_pc.next = 0b0
                if RAMdone == 1:
                    ok_pc.next = 1
                    EstadoPresente.next = Estado.Fetch

            else:   
                # Esto es para cuando inicie la maquina de estado, habilitara el enable del PC y empezaremos en Fetch.
                RAMwrite.next = 0b0
                RAMread.next = 0b0
                Demux_Sel.next = 0b0
                Mux5_Sel.next = 0b0
                MBR_go.next = 0b0
                RegOk.next = 0b0
                ok_pc.next = 1
                EstadoPresente.next = Estado.Fetch
                # raise ValueError("Undefined state") #Cambien esto porque ni de vaina va a convertir a Verilog

    return Logic

def convert_FSM(hdl):

    # Inicialización de las entradas y salidas.
    clk = Signal(bool(0))
    reset = ResetSignal(0, active = 1, async=True)
    OPcode = Signal(modbv(0)[7:0])
    RAMdone = Signal(modbv(0)[1:0])
    RAMwrite = Signal(modbv(0)[1:0])
    RAMread = Signal(modbv(0)[1:0])
    Demux_Sel = Signal(modbv(0)[1:0])
    Mux5_Sel = Signal(modbv(0)[1:0])
    MBR_go = Signal(modbv(0)[1:0])
    RegOk = Signal(modbv(0)[1:0])
    ok_pc = Signal(modbv(0)[1:0])

    convertFSM = FSM(clk, reset, OPcode, RAMdone, RAMwrite, RAMread, Demux_Sel, Mux5_Sel, MBR_go, RegOk, ok_pc)
    convertFSM.convert(hdl=hdl)

if __name__ == '__main__':

	convert_FSM(hdl='verilog')
