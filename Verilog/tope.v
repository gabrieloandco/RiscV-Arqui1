// File: tope.v
// Generated by MyHDL 1.0dev
// Date: Tue Nov 29 13:03:58 2016


`timescale 1ns/10ps

module tope (
    clk,
    reset,
    DataOutRAM,
    Done,
    Address,
    DataInRAM,
    WR,
    WE,
    RE
);


input clk;
input reset;
input [31:0] DataOutRAM;
input Done;
output [4:0] Address;
reg [4:0] Address;
output [31:0] DataInRAM;
reg [31:0] DataInRAM;
output [3:0] WR;
reg [3:0] WR;
output WE;
reg WE;
output RE;
reg RE;

reg [0:0] PCsrc;
reg [2:0] Dwidth;
reg [31:0] r1d;
wire [4:0] rd;
reg [0:0] RegWrite;
reg [0:0] Reg_OK;
wire [2:0] funct3;
wire [4:0] rs1;
wire [31:0] mux1_010;
wire [6:0] Opcode;
reg [31:0] PCEN_BHW;
wire [31:0] mux1_001;
wire [6:0] funct7;
wire [4:0] rs2;
reg [0:0] ALUsrc;
wire [31:0] add2_mux4;
reg [2:0] RegDest;
wire [0:0] RegEnable;
reg [31:0] mux3_add2;
reg [31:0] ALUout;
reg [31:0] mux4_PC;
reg [31:0] mux1_011;
wire [31:0] datainstruccion;
wire [31:0] dirdatos;
wire [1:0] BHWDIR;
reg [31:0] datainmediato;
reg [31:0] rdd;
wire [31:0] mux1_000;
reg [0:0] ALUflag;
reg [0:0] Sel_Mux;
reg [31:0] ALUinA;
reg [0:0] Ok_PC;
reg [3:0] ALUop;
reg [0:0] ConvInst_1_bit31;
reg [19:0] ConvInst_1_bit31_12;
reg [5:0] ConvInst_1_bit10_5;
reg [3:0] ConvInst_1_bit4_1;
reg [11:0] ConvInst_1_bit11_0;
reg [0:0] ConvInst_1_bit0;
reg [20:0] ConvInst_1_bit31_11;
reg [0:0] ConvInst_1_bit11;
reg [10:0] ConvInst_1_bit30_20;
reg [7:0] ConvInst_1_bit19_12;
reg [11:0] ConvInst_1_bit31_20;
reg [31:0] CPR_1_Demux_MBR;
reg [0:0] CPR_1_MBR_go;
reg [0:0] CPR_1_Mux5_Sel;
reg [0:0] CPR_1_Demux_Sel;
reg [31:0] CPR_1_MBR_1_register;
reg [1:0] CPR_1_FSM_1_EstadoPresente;
wire [7:0] BHW_1_data24_16;
wire [15:0] BHW_1_data32_16;
wire [7:0] BHW_1_data32_24;
wire [7:0] BHW_1_data8_0;
wire [7:0] BHW_1_data16_8;
wire [15:0] BHW_1_data16_0;
reg [31:0] PC_1_register;
reg [31:0] RegisterFile_1_regs [0:32-1];




assign mux1_000 = (dirdatos + 4);


always @(PCsrc, add2_mux4, ALUout) begin: TOPE_MUX4_1_BEHAVIOR_MUX4
    if ((PCsrc == 0)) begin
        mux4_PC = {ALUout[32-1:1], (0 != 0)};
    end
    else begin
        mux4_PC = add2_mux4;
    end
end



assign add2_mux4 = (mux3_add2 + dirdatos);


always @(datainstruccion) begin: TOPE_CONVINST_1_ASSIGNMENT
    if (((datainstruccion[7-1:0] == 3) || (datainstruccion[7-1:0] == 19) || (datainstruccion[7-1:0] == 111))) begin
        // convierte de instruccion al inmediato de I
        ConvInst_1_bit31_11 = {datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31]};
        ConvInst_1_bit10_5 = datainstruccion[31-1:25];
        ConvInst_1_bit4_1 = datainstruccion[25-1:21];
        ConvInst_1_bit0 = datainstruccion[20];
        ConvInst_1_bit11 = 0;
        ConvInst_1_bit31_12 = 0;
        ConvInst_1_bit31 = 0;
        ConvInst_1_bit30_20 = 0;
        ConvInst_1_bit19_12 = 0;
        ConvInst_1_bit11_0 = 0;
        ConvInst_1_bit31_20 = 0;
    end
    else if ((datainstruccion[7-1:0] == 35)) begin
        // convierte de instruccion al inmediato de S
        ConvInst_1_bit31_11 = {datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31]};
        ConvInst_1_bit10_5 = datainstruccion[31-1:25];
        ConvInst_1_bit4_1 = datainstruccion[12-1:8];
        ConvInst_1_bit0 = datainstruccion[7];
        ConvInst_1_bit11 = 0;
        ConvInst_1_bit31_12 = 0;
        ConvInst_1_bit31 = 0;
        ConvInst_1_bit30_20 = 0;
        ConvInst_1_bit19_12 = 0;
        ConvInst_1_bit11_0 = 0;
        ConvInst_1_bit31_20 = 0;
    end
    else if ((datainstruccion[7-1:0] == 99)) begin
        // convierte de instruccion al inmediato de B
        ConvInst_1_bit31_12 = {datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31]};
        ConvInst_1_bit11 = datainstruccion[7];
        ConvInst_1_bit10_5 = datainstruccion[31-1:25];
        ConvInst_1_bit4_1 = datainstruccion[12-1:8];
        ConvInst_1_bit0 = (0 != 0);
        ConvInst_1_bit31_11 = 0;
        ConvInst_1_bit31 = 0;
        ConvInst_1_bit30_20 = 0;
        ConvInst_1_bit19_12 = 0;
        ConvInst_1_bit11_0 = 0;
        ConvInst_1_bit31_20 = 0;
    end
    else if (((datainstruccion[7-1:0] == 55) || (datainstruccion[7-1:0] == 23))) begin
        // Obtiene el inmediato para las instrucciones de formato U
        ConvInst_1_bit31 = datainstruccion[31];
        ConvInst_1_bit30_20 = datainstruccion[31-1:20];
        ConvInst_1_bit19_12 = datainstruccion[20-1:12];
        ConvInst_1_bit11_0 = {(0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0)};
        ConvInst_1_bit31_11 = 0;
        ConvInst_1_bit10_5 = 0;
        ConvInst_1_bit4_1 = 0;
        ConvInst_1_bit0 = 0;
        ConvInst_1_bit11 = 0;
        ConvInst_1_bit31_12 = 0;
        ConvInst_1_bit31_20 = 0;
    end
    else if ((datainstruccion[7-1:0] == 103)) begin
        // convierte de instruccion a J
        ConvInst_1_bit31_20 = {datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31], datainstruccion[31]};
        ConvInst_1_bit19_12 = datainstruccion[20-1:12];
        ConvInst_1_bit11 = datainstruccion[20];
        ConvInst_1_bit10_5 = datainstruccion[31-1:25];
        ConvInst_1_bit4_1 = datainstruccion[25-1:21];
        ConvInst_1_bit0 = (0 != 0);
        ConvInst_1_bit31_11 = 0;
        ConvInst_1_bit31_12 = 0;
        ConvInst_1_bit31 = 0;
        ConvInst_1_bit30_20 = 0;
        ConvInst_1_bit11_0 = 0;
    end
    else begin
        ConvInst_1_bit31_11 = 0;
        ConvInst_1_bit10_5 = 0;
        ConvInst_1_bit4_1 = 0;
        ConvInst_1_bit0 = 0;
        ConvInst_1_bit11 = 0;
        ConvInst_1_bit31_12 = 0;
        ConvInst_1_bit31 = 0;
        ConvInst_1_bit30_20 = 0;
        ConvInst_1_bit19_12 = 0;
        ConvInst_1_bit11_0 = 0;
        ConvInst_1_bit31_20 = 0;
    end
end


always @(ConvInst_1_bit31, datainstruccion, ConvInst_1_bit31_12, ConvInst_1_bit10_5, ConvInst_1_bit0, ConvInst_1_bit31_11, ConvInst_1_bit4_1, ConvInst_1_bit11, ConvInst_1_bit30_20, ConvInst_1_bit31_20, ConvInst_1_bit19_12, ConvInst_1_bit11_0) begin: TOPE_CONVINST_1_CONCATENACION
    if (((datainstruccion[7-1:0] == 3) || (datainstruccion[7-1:0] == 19) || (datainstruccion[7-1:0] == 111))) begin
        datainmediato = {ConvInst_1_bit31_11, ConvInst_1_bit10_5, ConvInst_1_bit4_1, ConvInst_1_bit0};
    end
    else if ((datainstruccion[7-1:0] == 35)) begin
        datainmediato = {ConvInst_1_bit31_11, ConvInst_1_bit10_5, ConvInst_1_bit4_1, ConvInst_1_bit0};
    end
    else if ((datainstruccion[7-1:0] == 99)) begin
        datainmediato = {ConvInst_1_bit31_12, ConvInst_1_bit11, ConvInst_1_bit10_5, ConvInst_1_bit4_1, ConvInst_1_bit0};
    end
    else if (((datainstruccion[7-1:0] == 55) || (datainstruccion[7-1:0] == 23))) begin
        datainmediato = {ConvInst_1_bit31, ConvInst_1_bit30_20, ConvInst_1_bit19_12, ConvInst_1_bit11_0};
    end
    else if ((datainstruccion[7-1:0] == 103)) begin
        datainmediato = {ConvInst_1_bit31_20, ConvInst_1_bit19_12, ConvInst_1_bit11, ConvInst_1_bit10_5, ConvInst_1_bit4_1, ConvInst_1_bit0};
    end
    else begin
        datainmediato = datainstruccion;
    end
end


always @(posedge clk, posedge reset) begin: TOPE_CPR_1_MBR_1_WRITE
    if (reset == 1) begin
        CPR_1_MBR_1_register <= 0;
    end
    else begin
        if ((CPR_1_MBR_go == 1)) begin
            CPR_1_MBR_1_register <= CPR_1_Demux_MBR;
        end
        else if ((reset == 1)) begin
            CPR_1_MBR_1_register <= 0;
        end
        else begin
            CPR_1_MBR_1_register <= CPR_1_MBR_1_register;
        end
    end
end



assign datainstruccion = CPR_1_MBR_1_register;


always @(CPR_1_Demux_Sel, DataOutRAM) begin: TOPE_CPR_1_DEMUX_1_BEHAVIOR_DEMUX
    CPR_1_Demux_MBR = 0;
    PCEN_BHW = 0;
    if ((CPR_1_Demux_Sel == 0)) begin
        CPR_1_Demux_MBR = DataOutRAM;
    end
    else begin
        PCEN_BHW = DataOutRAM;
    end
end


always @(posedge clk, posedge reset) begin: TOPE_CPR_1_FSM_1_LOGIC
    if (reset == 1) begin
        CPR_1_Demux_Sel <= 0;
        Ok_PC <= 0;
        RE <= 0;
        Reg_OK <= 0;
        CPR_1_MBR_go <= 0;
        WE <= 0;
        CPR_1_FSM_1_EstadoPresente <= 0;
        CPR_1_Mux5_Sel <= 0;
    end
    else begin
        if ((reset == 1)) begin
            WE <= 0;
            RE <= 0;
            CPR_1_Demux_Sel <= 0;
            CPR_1_Mux5_Sel <= 0;
            CPR_1_MBR_go <= 0;
            Reg_OK <= 0;
            Ok_PC <= 1;
            CPR_1_FSM_1_EstadoPresente <= 0;
        end
        else begin
            case (CPR_1_FSM_1_EstadoPresente)
                'h0: begin
                    WE <= 0;
                    RE <= 1;
                    CPR_1_Demux_Sel <= 0;
                    CPR_1_Mux5_Sel <= 0;
                    CPR_1_MBR_go <= 0;
                    Reg_OK <= 0;
                    Ok_PC <= 0;
                    if ((Done == 1)) begin
                        CPR_1_MBR_go <= 1;
                        CPR_1_FSM_1_EstadoPresente <= 1;
                    end
                end
                'h1: begin
                    WE <= 0;
                    RE <= 0;
                    CPR_1_Demux_Sel <= 0;
                    CPR_1_Mux5_Sel <= 0;
                    CPR_1_MBR_go <= 0;
                    Reg_OK <= 0;
                    Ok_PC <= 0;
                    if (((Opcode != 3) && (Opcode != 35))) begin
                        Ok_PC <= 1;
                        Reg_OK <= 1;
                        CPR_1_FSM_1_EstadoPresente <= 0;
                    end
                    else if ((Opcode == 3)) begin
                        CPR_1_FSM_1_EstadoPresente <= 2;
                    end
                    else if ((Opcode == 35)) begin
                        CPR_1_FSM_1_EstadoPresente <= 3;
                    end
                end
                'h2: begin
                    WE <= 1;
                    RE <= 1;
                    CPR_1_Demux_Sel <= 1;
                    CPR_1_Mux5_Sel <= 1;
                    CPR_1_MBR_go <= 0;
                    Reg_OK <= 0;
                    Ok_PC <= 0;
                    if ((Done == 1)) begin
                        Ok_PC <= 1;
                        Reg_OK <= 1;
                        CPR_1_FSM_1_EstadoPresente <= 0;
                    end
                end
                'h3: begin
                    WE <= 1;
                    RE <= 1;
                    CPR_1_Demux_Sel <= 0;
                    CPR_1_Mux5_Sel <= 1;
                    CPR_1_MBR_go <= 0;
                    Reg_OK <= 0;
                    Ok_PC <= 0;
                    if ((Done == 1)) begin
                        Ok_PC <= 1;
                        CPR_1_FSM_1_EstadoPresente <= 0;
                    end
                end
                default: begin
                    WE <= 0;
                    RE <= 0;
                    CPR_1_Demux_Sel <= 0;
                    CPR_1_Mux5_Sel <= 0;
                    CPR_1_MBR_go <= 0;
                    Reg_OK <= 0;
                    Ok_PC <= 1;
                    CPR_1_FSM_1_EstadoPresente <= 0;
                end
            endcase
        end
    end
end


always @(dirdatos, CPR_1_Mux5_Sel, ALUout) begin: TOPE_CPR_1_MUX2_2_BEHAVIOR_MUX2
    if ((CPR_1_Mux5_Sel == 0)) begin
        Address = dirdatos;
    end
    else begin
        Address = ALUout;
    end
end

// Datain son los 2 bits menos significativos de la salida de la ALU.
// A continuacion una tabla indicando todas las posibles combinaciones del ultimo numero 
// hexadecimal de la direccion a la RAM en bits, y para cada uno de ellos la salida sera un enabler de escritura
// de la RAM (enabler de escritura por byte).
always @(Dwidth, BHWDIR) begin: TOPE_STOREENABLE_1_SELECTOR
    if (((Dwidth == 0) || (Dwidth == 3))) begin
        case (BHWDIR)
            'h0: begin
                WR = 1;
            end
            'h1: begin
                WR = 2;
            end
            'h2: begin
                WR = 4;
            end
            'h3: begin
                WR = 8;
            end
            default: begin
                WR = 0;
            end
        endcase
    end
    else if (((Dwidth == 1) || (Dwidth == 4))) begin
        if (((BHWDIR == 0) || (BHWDIR == 1))) begin
            WR = 3;
        end
        if (((BHWDIR == 2) || (BHWDIR == 3))) begin
            WR = 12;
        end
        else begin
            WR = 0;
        end
    end
    else if ((Dwidth == 2)) begin
        WR = 15;
    end
    else begin
        WR = 0;
    end
end



assign BHW_1_data8_0 = PCEN_BHW[8-1:0];
assign BHW_1_data16_8 = PCEN_BHW[16-1:8];
assign BHW_1_data24_16 = PCEN_BHW[24-1:16];
assign BHW_1_data32_24 = PCEN_BHW[32-1:24];
assign BHW_1_data16_0 = PCEN_BHW[16-1:0];
assign BHW_1_data32_16 = PCEN_BHW[32-1:16];


always @(BHW_1_data24_16, BHW_1_data8_0, PCEN_BHW, BHW_1_data32_24, BHWDIR, Dwidth, BHW_1_data32_16, BHW_1_data16_8, BHW_1_data16_0) begin: TOPE_BHW_1_BEHAVIORBHW
    case (Dwidth)
        'h0: begin
            case (BHWDIR)
                'h0: begin
                    mux1_011 = {PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], BHW_1_data8_0};
                end
                'h1: begin
                    mux1_011 = {PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], BHW_1_data16_8};
                end
                'h2: begin
                    mux1_011 = {PCEN_BHW[23], PCEN_BHW[23], PCEN_BHW[23], PCEN_BHW[23], PCEN_BHW[23], PCEN_BHW[23], PCEN_BHW[23], PCEN_BHW[23], PCEN_BHW[23], PCEN_BHW[23], PCEN_BHW[23], PCEN_BHW[23], PCEN_BHW[23], PCEN_BHW[23], PCEN_BHW[23], PCEN_BHW[23], PCEN_BHW[23], PCEN_BHW[23], PCEN_BHW[23], PCEN_BHW[23], PCEN_BHW[23], PCEN_BHW[23], PCEN_BHW[23], PCEN_BHW[23], BHW_1_data24_16};
                end
                'h3: begin
                    mux1_011 = {PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], BHW_1_data32_24};
                end
                default: begin
                    mux1_011 = {PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], PCEN_BHW[7], BHW_1_data8_0};
                end
            endcase
        end
        'h1: begin
            if (((BHWDIR == 0) || (BHWDIR == 1))) begin
                mux1_011 = {PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], BHW_1_data16_0};
            end
            else if (((BHWDIR == 2) || (BHWDIR == 3))) begin
                mux1_011 = {PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], PCEN_BHW[31], BHW_1_data32_16};
            end
            else begin
                mux1_011 = {PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], PCEN_BHW[15], BHW_1_data16_0};
            end
        end
        'h2: begin
            mux1_011 = PCEN_BHW;
        end
        'h3: begin
            case (BHWDIR)
                'h0: begin
                    mux1_011 = {(0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), BHW_1_data8_0};
                end
                'h1: begin
                    mux1_011 = {(0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), BHW_1_data16_8};
                end
                'h2: begin
                    mux1_011 = {(0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), BHW_1_data24_16};
                end
                'h3: begin
                    mux1_011 = {(0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), BHW_1_data32_24};
                end
                default: begin
                    mux1_011 = {(0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), BHW_1_data8_0};
                end
            endcase
        end
        'h4: begin
            if (((BHWDIR == 0) || (BHWDIR == 1))) begin
                mux1_011 = {(0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), BHW_1_data16_0};
            end
            else if (((BHWDIR == 2) || (BHWDIR == 3))) begin
                mux1_011 = {(0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), BHW_1_data32_16};
            end
            else begin
                mux1_011 = {(0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), BHW_1_data16_0};
            end
        end
        default: begin
            mux1_011 = PCEN_BHW;
        end
    endcase
end



assign mux1_001 = (dirdatos + datainmediato);


always @(mux1_011, mux1_010, mux1_001, mux1_000, ALUout, RegDest) begin: TOPE_MUX1_1_BEHAVIOR_MUX1
    case (RegDest)
        'h0: begin
            rdd = mux1_000;
        end
        'h1: begin
            rdd = mux1_001;
        end
        'h2: begin
            rdd = mux1_010;
        end
        'h3: begin
            rdd = mux1_011;
        end
        'h4: begin
            rdd = ALUout;
        end
        default: begin
            rdd = 0;
        end
    endcase
end


always @(ALUinA, r1d, ALUop) begin: TOPE_ALU_1_OUTPUT
    ALUflag = 0;
    case (ALUop)
        'h0: begin
            ALUout = (ALUinA + r1d);
            if (((ALUinA + r1d) == 0)) begin
                ALUflag = 1;
            end
        end
        'h1: begin
            ALUout = (ALUinA - r1d);
            if ((($signed({1'b0, ALUinA}) - $signed({1'b0, r1d})) == 0)) begin
                ALUflag = 1;
            end
        end
        'h2: begin
            ALUout = (ALUinA ^ r1d);
            if (((ALUinA ^ r1d) == 0)) begin
                ALUflag = 1;
            end
        end
        'h3: begin
            ALUout = (ALUinA | r1d);
            if (((ALUinA | r1d) == 0)) begin
                ALUflag = 1;
            end
        end
        'h4: begin
            ALUout = (ALUinA & r1d);
            if (((ALUinA & r1d) == 0)) begin
                ALUflag = 1;
            end
        end
        'h5: begin
            ALUout = (ALUinA >>> r1d[5-1:0]);
            if (((ALUinA >>> r1d[5-1:0]) == 0)) begin
                ALUflag = 1;
            end
        end
        'h6: begin
            ALUout = (ALUinA << r1d[5-1:0]);
            if (((ALUinA << r1d[5-1:0]) == 0)) begin
                ALUflag = 1;
            end
        end
        'h7: begin
            ALUout = $signed($signed(ALUinA) >>> r1d[5-1:0]);
            if (($signed($signed(ALUinA) >>> r1d[5-1:0]) == 0)) begin
                ALUflag = 1;
            end
        end
        'h8: begin
            if ((($signed(ALUinA) - $signed(r1d)) < 0)) begin
                ALUout = 32'h1;
            end
            else begin
                ALUout = 32'h0;
                ALUflag = 1;
            end
        end
        'h9: begin
            if ((($signed({1'b0, ALUinA}) - $signed({1'b0, r1d})) < 0)) begin
                ALUout = 32'h1;
            end
            else begin
                ALUout = 32'h0;
                ALUflag = 1;
            end
        end
        'ha: begin
            if ((ALUinA == r1d)) begin
                ALUout = 32'h1;
            end
            else begin
                ALUout = 32'h0;
                ALUflag = 1;
            end
        end
        'hb: begin
            if ((ALUinA != r1d)) begin
                ALUout = 32'h1;
            end
            else begin
                ALUout = 32'h0;
                ALUflag = 1;
            end
        end
        'hc: begin
            if ((($signed(ALUinA) - $signed(r1d)) < 0)) begin
                ALUout = 32'h0;
                ALUflag = 1;
            end
            else begin
                ALUout = 32'h1;
            end
        end
        'hd: begin
            if ((($signed({1'b0, ALUinA}) - $signed({1'b0, r1d})) < 0)) begin
                ALUout = 32'h0;
                ALUflag = 1;
            end
            else begin
                ALUout = 32'h1;
            end
        end
        'he: begin
            if ((($signed(ALUinA) - $signed(r1d)) < 0)) begin
                ALUout = 32'h1;
            end
            else begin
                ALUout = 32'h0;
                ALUflag = 1;
            end
        end
        'hf: begin
            if ((($signed({1'b0, ALUinA}) - $signed({1'b0, r1d})) < 0)) begin
                ALUout = 32'h1;
            end
            else begin
                ALUout = 32'h0;
                ALUflag = 1;
            end
        end
    endcase
end


always @(DataInRAM, ALUsrc, datainmediato) begin: TOPE_MUX2_1_BEHAVIOR_MUX2
    if ((ALUsrc == 0)) begin
        ALUinA = DataInRAM;
    end
    else begin
        ALUinA = datainmediato;
    end
end


always @(posedge clk, posedge reset) begin: TOPE_PC_1_WRITE
    if (reset == 1) begin
        PC_1_register <= 0;
    end
    else begin
        if ((Ok_PC == 1)) begin
            PC_1_register <= mux4_PC;
        end
        else if ((reset == 1)) begin
            PC_1_register <= 0;
        end
        else begin
            PC_1_register <= PC_1_register;
        end
    end
end



assign dirdatos = PC_1_register;



assign RegEnable = (RegWrite & Reg_OK);

// Para el set de instrucciones de tipo R es necesaria la funct3 y funct7, pero para el funcionamiento del codigo 
// no es estrictamente necesario. Por esa razón la mayoria de los condiciones dentro de if OPcode == C_OPcode.R_type 
// evaluan ambas codiciones.
// Para todas las operaciones tipo R ALUsrc.next = 0b0 y DWidth no es utilizado.
always @(ALUflag, funct3, Opcode, funct7) begin: TOPE_CONTROLUNIT_1_BEHAVIOR
    RegWrite = 0;
    RegDest = 4;
    ALUsrc = 0;
    ALUop = 0;
    Dwidth = 5;
    PCsrc = 1;
    Sel_Mux = 0;
    if ((Opcode == 51)) begin
        RegWrite = 1;
        RegDest = 4;
        ALUsrc = 0;
        PCsrc = 1;
        Sel_Mux = 0;
        if (((funct3 == 0) && (funct7 == 0))) begin
            ALUop = 0;
        end
        else if (((funct3 == 0) && (funct7 == 32))) begin
            ALUop = 1;
        end
        else if (((funct3 == 1) && (funct7 == 0))) begin
            ALUop = 6;
        end
        else if (((funct3 == 2) && (funct7 == 0))) begin
            ALUop = 8;
        end
        else if (((funct3 == 3) && (funct7 == 0))) begin
            ALUop = 9;
        end
        else if (((funct3 == 4) && (funct7 == 0))) begin
            ALUop = 2;
        end
        else if (((funct3 == 5) && (funct7 == 0))) begin
            ALUop = 5;
        end
        else if (((funct3 == 5) && (funct7 == 32))) begin
            ALUop = 7;
        end
        else if (((funct3 == 6) && (funct7 == 0))) begin
            ALUop = 3;
        end
        else if (((funct3 == 7) && (funct7 == 0))) begin
            ALUop = 4;
        end
        else begin
            ALUop = 0;
        end
    end
    // El set de instrucciones de tipo I posee instrucciones que usan un immediato de 12 bits (imm[11:0]) 
    // y unos que usan dos immediatos uno de 5 bits (imm[4:0] = shamt = shift amount), otro de 7 bits (imm[11:5]) que 
    // indica si usar SLLI/SRLI o SRAI
    // DWidth es irrelevante.
    if ((Opcode == 19)) begin
        RegWrite = 1;
        RegDest = 4;
        PCsrc = 1;
        ALUsrc = 1;
        Sel_Mux = 0;
        if ((funct3 == 0)) begin
            ALUop = 0;
        end
        else if ((funct3 == 2)) begin
            ALUop = 8;
        end
        else if ((funct3 == 3)) begin
            ALUop = 9;
        end
        else if ((funct3 == 4)) begin
            ALUop = 2;
        end
        else if ((funct3 == 6)) begin
            ALUop = 3;
        end
        else if ((funct3 == 7)) begin
            ALUop = 4;
        end
        else if (((funct3 == 1) && (funct7 == 0))) begin
            ALUop = 6;
        end
        else if (((funct3 == 5) && (funct7 == 0))) begin
            ALUop = 5;
        end
        else if (((funct3 == 5) && (funct7 == 32))) begin
            ALUop = 7;
        end
        else begin
            ALUop = 0;
        end
    end
    // En la instruccion JALR que es de tipo I se usa la operacion de ADD para sumar el registro de direccion rs1 con imm[11:0] de 12 bits, y colocar el 
    // LSB en 0, esto ultimo se realiza colocando el cable a tierra en el bus de datos, para no agregar una operacion mas a la ALU.
    // Para este tipo de instruccion no importa el valor que tenga la variable Dwidth, Sel_Mux.
    if (((Opcode == 103) && (funct3 == 0))) begin
        RegWrite = 1;
        RegDest = 0;
        ALUsrc = 1;
        ALUop = 0;
        PCsrc = 0;
    end
    // Para las instrucciones de carga (I_type_LOAD) se obtendra la dirección del dato a cargar sumando el inmediato (extendido con signo) con el registro rs1
    // y se recibe de la memoria un BYTE, HALFWORD o WORD dependiendo de la función el cual se extiende con signo o sin signo
    if ((Opcode == 3)) begin
        RegWrite = 1;
        RegDest = 3;
        ALUsrc = 1;
        ALUop = 0;
        PCsrc = 1;
        Sel_Mux = 0;
        case (funct3)
            'h0: begin
                Dwidth = 0;
            end
            'h1: begin
                Dwidth = 1;
            end
            'h2: begin
                Dwidth = 2;
            end
            'h4: begin
                Dwidth = 3;
            end
            'h5: begin
                Dwidth = 4;
            end
            default: begin
                Dwidth = 5;
            end
        endcase
    end
    // Para las instrucciones de tipo S (store) solo se ultiliza la escritura en la memoria, por lo que deshabilitamos RegWrite y las salidas
    // RegDest/ALUsrc/ALUop/Ext_E
    if ((Opcode == 35)) begin
        RegWrite = 0;
        RegDest = 3;
        ALUsrc = 1;
        ALUop = 0;
        Dwidth = 0;
        PCsrc = 1;
        Sel_Mux = 0;
        case (funct3)
            'h0: begin
                Dwidth = 0;
            end
            'h1: begin
                Dwidth = 1;
            end
            'h2: begin
                Dwidth = 2;
            end
            default: begin
                Dwidth = 5;
            end
        endcase
    end
    // Para la instruccion branch, tipo SB, se carga un inmediato para sumarlo a la direccion actual del PC, y este sera la siguiente instruccion siempre y cuando se cumpla
    // la condicion del branch (funct3) que sale de una comparacion exitosa de la ALU (flag branch). 
    // No son necesarios RegDest, Ext_E y DWidth. Deshabilitamos RegWrite. La operacion de la ALU dependera del funct3 y
    // Pcsrc dependera de si se cumple el branch o no.
    if ((Opcode == 99)) begin
        RegWrite = 0;
        ALUsrc = 0;
        PCsrc = 1;
        Sel_Mux = 1;
        case (funct3)
            'h0: begin
                ALUop = 10;
            end
            'h1: begin
                ALUop = 11;
            end
            'h4: begin
                ALUop = 12;
            end
            'h5: begin
                ALUop = 14;
            end
            'h6: begin
                ALUop = 13;
            end
            'h7: begin
                ALUop = 15;
            end
            default: begin
                ALUop = 0;
            end
        endcase
        if ((ALUflag == 1)) begin
            Sel_Mux = 1;
        end
        else begin
            Sel_Mux = 0;
        end
    end
    // Para la instruccion LUI, tipo U, se almacena un inmediato rellanado con 0's (Fill) en el registro deseado. Debemos habilitar la escritura en los registros (RegWrite=1), deshabilitar
    // la escritura y lectura de datos en la memoria RAM ya que no son necesarios, la siguiente instruccion de la PC es PC + 4 (PCsrc = 00) y seleccionamos la entrada
    // del fill a la escritura de los registros (RegDest=010). No son necesarrios ALUsrc, Ext_E ni DWidth.
    if ((Opcode == 55)) begin
        RegWrite = 1;
        RegDest = 2;
        PCsrc = 1;
        Sel_Mux = 0;
    end
    // Para la instruccion AUIPC, tipo U, tomamos un inmediato de 20 bits de la instruccion, rellenamos con 0's los bits menos significativos para completar los 32 bits (Fill), se lo sumamos a la direccion actual de la PC y
    // lo almacenamos en el registro deseado. Para esto, habilitamos la escritura de los registros, hacemos que la entrada del registro sea la sumatoria del FIll con la direccion de PC (RegDest=001).
    // La siguiente instruccion del PC es PC + 4, entonces PCsrc = 00 y deshabilitamos la escritura y lectura de datos de la memoria RAM ya que no son necesarios.
    if ((Opcode == 23)) begin
        RegWrite = 1;
        RegDest = 1;
        PCsrc = 1;
        Sel_Mux = 0;
    end
    // Para la instruccion JAL, tipo UJ, guardaremos la instruccion PC + 4 en el registro deseado. Ademas, tomamos un inmediato de la instruccion, la extendemos 
    // y se la sumamos a la direccion actual del PC. Este resultado sera la siguiente instruccion del PC. Para esto, habilitamos la escritura de los registros, 
    // hacemos que la entrada del registro sea PC + 4 (RegDest=000) y para indicar la siguiente instruccion del PC hacemos PCsrc = 1. Deshabilitamos la escritura
    // y lectura de datos de la memoria RAM ya que no son necesarios.
    // ALUsrc, ALUop, DWidth no son necesarios.
    if ((Opcode == 111)) begin
        RegWrite = 1;
        RegDest = 0;
        PCsrc = 1;
        Sel_Mux = 1;
    end
end


always @(Sel_Mux, datainmediato) begin: TOPE_MUX3_1_BEHAVIOR_MUX3
    if ((Sel_Mux == 0)) begin
        mux3_add2 = 4;
    end
    else begin
        mux3_add2 = datainmediato;
    end
end



assign rd = datainstruccion[12-1:7];
assign rs2 = datainstruccion[25-1:20];
assign rs1 = datainstruccion[20-1:15];
assign mux1_010 = datainmediato;
assign Opcode = datainstruccion[7-1:0];
assign funct7 = datainstruccion[32-1:25];
assign funct3 = datainstruccion[15-1:12];
assign BHWDIR = ALUout[2-1:0];


always @(posedge clk, posedge reset) begin: TOPE_REGISTERFILE_1_WRITE
    if (reset == 1) begin
        RegisterFile_1_regs[0] <= 0;
        RegisterFile_1_regs[1] <= 0;
        RegisterFile_1_regs[2] <= 0;
        RegisterFile_1_regs[3] <= 0;
        RegisterFile_1_regs[4] <= 0;
        RegisterFile_1_regs[5] <= 0;
        RegisterFile_1_regs[6] <= 0;
        RegisterFile_1_regs[7] <= 0;
        RegisterFile_1_regs[8] <= 0;
        RegisterFile_1_regs[9] <= 0;
        RegisterFile_1_regs[10] <= 0;
        RegisterFile_1_regs[11] <= 0;
        RegisterFile_1_regs[12] <= 0;
        RegisterFile_1_regs[13] <= 0;
        RegisterFile_1_regs[14] <= 0;
        RegisterFile_1_regs[15] <= 0;
        RegisterFile_1_regs[16] <= 0;
        RegisterFile_1_regs[17] <= 0;
        RegisterFile_1_regs[18] <= 0;
        RegisterFile_1_regs[19] <= 0;
        RegisterFile_1_regs[20] <= 0;
        RegisterFile_1_regs[21] <= 0;
        RegisterFile_1_regs[22] <= 0;
        RegisterFile_1_regs[23] <= 0;
        RegisterFile_1_regs[24] <= 0;
        RegisterFile_1_regs[25] <= 0;
        RegisterFile_1_regs[26] <= 0;
        RegisterFile_1_regs[27] <= 0;
        RegisterFile_1_regs[28] <= 0;
        RegisterFile_1_regs[29] <= 0;
        RegisterFile_1_regs[30] <= 0;
        RegisterFile_1_regs[31] <= 0;
    end
    else begin
        if (((rd != 0) && (RegEnable == 1) && (reset == 0))) begin
            RegisterFile_1_regs[rd] <= rdd;
        end
        else if ((reset == 1)) begin
            RegisterFile_1_regs[0] <= 0;
            RegisterFile_1_regs[1] <= 0;
            RegisterFile_1_regs[2] <= 0;
            RegisterFile_1_regs[3] <= 0;
            RegisterFile_1_regs[4] <= 0;
            RegisterFile_1_regs[5] <= 0;
            RegisterFile_1_regs[6] <= 0;
            RegisterFile_1_regs[7] <= 0;
            RegisterFile_1_regs[8] <= 0;
            RegisterFile_1_regs[9] <= 0;
            RegisterFile_1_regs[10] <= 0;
            RegisterFile_1_regs[11] <= 0;
            RegisterFile_1_regs[12] <= 0;
            RegisterFile_1_regs[13] <= 0;
            RegisterFile_1_regs[14] <= 0;
            RegisterFile_1_regs[15] <= 0;
            RegisterFile_1_regs[16] <= 0;
            RegisterFile_1_regs[17] <= 0;
            RegisterFile_1_regs[18] <= 0;
            RegisterFile_1_regs[19] <= 0;
            RegisterFile_1_regs[20] <= 0;
            RegisterFile_1_regs[21] <= 0;
            RegisterFile_1_regs[22] <= 0;
            RegisterFile_1_regs[23] <= 0;
            RegisterFile_1_regs[24] <= 0;
            RegisterFile_1_regs[25] <= 0;
            RegisterFile_1_regs[26] <= 0;
            RegisterFile_1_regs[27] <= 0;
            RegisterFile_1_regs[28] <= 0;
            RegisterFile_1_regs[29] <= 0;
            RegisterFile_1_regs[30] <= 0;
            RegisterFile_1_regs[31] <= 0;
        end
        else begin
            RegisterFile_1_regs[rd] <= RegisterFile_1_regs[rd];
        end
    end
end


always @(RegisterFile_1_regs[0], RegisterFile_1_regs[1], RegisterFile_1_regs[2], RegisterFile_1_regs[3], RegisterFile_1_regs[4], RegisterFile_1_regs[5], RegisterFile_1_regs[6], RegisterFile_1_regs[7], RegisterFile_1_regs[8], RegisterFile_1_regs[9], RegisterFile_1_regs[10], RegisterFile_1_regs[11], RegisterFile_1_regs[12], RegisterFile_1_regs[13], RegisterFile_1_regs[14], RegisterFile_1_regs[15], RegisterFile_1_regs[16], RegisterFile_1_regs[17], RegisterFile_1_regs[18], RegisterFile_1_regs[19], RegisterFile_1_regs[20], RegisterFile_1_regs[21], RegisterFile_1_regs[22], RegisterFile_1_regs[23], RegisterFile_1_regs[24], RegisterFile_1_regs[25], RegisterFile_1_regs[26], RegisterFile_1_regs[27], RegisterFile_1_regs[28], RegisterFile_1_regs[29], RegisterFile_1_regs[30], RegisterFile_1_regs[31], rs1, rs2) begin: TOPE_REGISTERFILE_1_READ
    if ((rs1 == 0)) begin
        r1d = 0;
    end
    else begin
        r1d = RegisterFile_1_regs[rs1];
    end
    if ((rs2 == 0)) begin
        DataInRAM = 0;
    end
    else begin
        DataInRAM = RegisterFile_1_regs[rs2];
    end
end

endmodule
