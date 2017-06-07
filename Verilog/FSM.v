// File: FSM.v
// Generated by MyHDL 1.0dev
// Date: Tue Nov 29 06:40:07 2016


`timescale 1ns/10ps

module FSM (
    clk,
    reset,
    OPcode,
    RAMdone,
    RAMwrite,
    RAMread,
    Demux_Sel,
    Mux5_Sel,
    MBR_go,
    RegOk,
    ok_pc
);
// Entradas: OPcode de 7 bits.
//           RAMdone de 1 bit.
//           clk de 1 bit
//           reset de 1 bit
// Salidas: RAMwrite  de 1 bit.
//          RAMread de 1 bit.
//          Demux_Sel de 1 bit.
//          Mux5_Sel de 1 bit.
//          MBR_go de 1 bit.
//          RegOk de 1 bit.
//          ok_pc de 1 bit

input clk;
input reset;
input [6:0] OPcode;
input [0:0] RAMdone;
output [0:0] RAMwrite;
reg [0:0] RAMwrite;
output [0:0] RAMread;
reg [0:0] RAMread;
output [0:0] Demux_Sel;
reg [0:0] Demux_Sel;
output [0:0] Mux5_Sel;
reg [0:0] Mux5_Sel;
output [0:0] MBR_go;
reg [0:0] MBR_go;
output [0:0] RegOk;
reg [0:0] RegOk;
output [0:0] ok_pc;
reg [0:0] ok_pc;

reg [1:0] EstadoPresente;



always @(posedge clk, posedge reset) begin: FSM_LOGIC
    if (reset == 1) begin
        MBR_go <= 0;
        RAMwrite <= 0;
        RegOk <= 0;
        RAMread <= 0;
        ok_pc <= 0;
        Mux5_Sel <= 0;
        EstadoPresente <= 0;
        Demux_Sel <= 0;
    end
    else begin
        if ((reset == 1)) begin
            RAMwrite <= 0;
            RAMread <= 0;
            Demux_Sel <= 0;
            Mux5_Sel <= 0;
            MBR_go <= 0;
            RegOk <= 0;
            ok_pc <= 1;
            EstadoPresente <= 0;
        end
        else begin
            case (EstadoPresente)
                'h0: begin
                    RAMwrite <= 0;
                    RAMread <= 1;
                    Demux_Sel <= 0;
                    Mux5_Sel <= 0;
                    MBR_go <= 0;
                    RegOk <= 0;
                    ok_pc <= 0;
                    if ((RAMdone == 1)) begin
                        MBR_go <= 1;
                        EstadoPresente <= 1;
                    end
                end
                'h1: begin
                    RAMwrite <= 0;
                    RAMread <= 0;
                    Demux_Sel <= 0;
                    Mux5_Sel <= 0;
                    MBR_go <= 0;
                    RegOk <= 0;
                    ok_pc <= 0;
                    if (((OPcode != 3) && (OPcode != 35))) begin
                        ok_pc <= 1;
                        RegOk <= 1;
                        EstadoPresente <= 0;
                    end
                    else if ((OPcode == 3)) begin
                        EstadoPresente <= 2;
                    end
                    else if ((OPcode == 35)) begin
                        EstadoPresente <= 3;
                    end
                end
                'h2: begin
                    RAMwrite <= 1;
                    RAMread <= 1;
                    Demux_Sel <= 1;
                    Mux5_Sel <= 1;
                    MBR_go <= 0;
                    RegOk <= 0;
                    ok_pc <= 0;
                    if ((RAMdone == 1)) begin
                        ok_pc <= 1;
                        RegOk <= 1;
                        EstadoPresente <= 0;
                    end
                end
                'h3: begin
                    RAMwrite <= 1;
                    RAMread <= 1;
                    Demux_Sel <= 0;
                    Mux5_Sel <= 1;
                    MBR_go <= 0;
                    RegOk <= 0;
                    ok_pc <= 0;
                    if ((RAMdone == 1)) begin
                        ok_pc <= 1;
                        EstadoPresente <= 0;
                    end
                end
                default: begin
                    RAMwrite <= 0;
                    RAMread <= 0;
                    Demux_Sel <= 0;
                    Mux5_Sel <= 0;
                    MBR_go <= 0;
                    RegOk <= 0;
                    ok_pc <= 1;
                    EstadoPresente <= 0;
                end
            endcase
        end
    end
end

endmodule