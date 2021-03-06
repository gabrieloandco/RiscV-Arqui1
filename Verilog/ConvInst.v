// File: ConvInst.v
// Generated by MyHDL 1.0dev
// Date: Tue Nov 29 05:00:49 2016


`timescale 1ns/10ps

module ConvInst (
    datain,
    dataout
);
// convierte a la instruccion deseada dependiendo del opcode
// opcode tipo I: Load:0000011, Aritmeticas:0010011,para JAL:1101111
// opcode tipo S:0100011
// opcode tipo B:1100011
// opcode tipo U:para LUI:0110111, para AUIPC:0010111
// opcode tipo J:1101111

input [31:0] datain;
output [31:0] dataout;
reg [31:0] dataout;

reg [0:0] bit0;
reg [7:0] bit19_12;
reg [11:0] bit11_0;
reg [5:0] bit10_5;
reg [11:0] bit31_20;
reg [19:0] bit31_12;
reg [3:0] bit4_1;
reg [20:0] bit31_11;
reg [0:0] bit11;
reg [0:0] bit31;
reg [10:0] bit30_20;



always @(datain) begin: CONVINST_ASSIGNMENT
    if (((datain[7-1:0] == 3) || (datain[7-1:0] == 19) || (datain[7-1:0] == 111))) begin
        // convierte de instruccion al inmediato de I
        bit31_11 = {datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31]};
        bit10_5 = datain[31-1:25];
        bit4_1 = datain[25-1:21];
        bit0 = datain[20];
        bit11 = 0;
        bit31_12 = 0;
        bit31 = 0;
        bit30_20 = 0;
        bit19_12 = 0;
        bit11_0 = 0;
        bit31_20 = 0;
    end
    else if ((datain[7-1:0] == 35)) begin
        // convierte de instruccion al inmediato de S
        bit31_11 = {datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31]};
        bit10_5 = datain[31-1:25];
        bit4_1 = datain[12-1:8];
        bit0 = datain[7];
        bit11 = 0;
        bit31_12 = 0;
        bit31 = 0;
        bit30_20 = 0;
        bit19_12 = 0;
        bit11_0 = 0;
        bit31_20 = 0;
    end
    else if ((datain[7-1:0] == 99)) begin
        // convierte de instruccion al inmediato de B
        bit31_12 = {datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31]};
        bit11 = datain[7];
        bit10_5 = datain[31-1:25];
        bit4_1 = datain[12-1:8];
        bit0 = (0 != 0);
        bit31_11 = 0;
        bit31 = 0;
        bit30_20 = 0;
        bit19_12 = 0;
        bit11_0 = 0;
        bit31_20 = 0;
    end
    else if (((datain[7-1:0] == 55) || (datain[7-1:0] == 23))) begin
        // Obtiene el inmediato para las instrucciones de formato U
        bit31 = datain[31];
        bit30_20 = datain[31-1:20];
        bit19_12 = datain[20-1:12];
        bit11_0 = {(0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0), (0 != 0)};
        bit31_11 = 0;
        bit10_5 = 0;
        bit4_1 = 0;
        bit0 = 0;
        bit11 = 0;
        bit31_12 = 0;
        bit31_20 = 0;
    end
    else if ((datain[7-1:0] == 103)) begin
        // convierte de instruccion a J
        bit31_20 = {datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31], datain[31]};
        bit19_12 = datain[20-1:12];
        bit11 = datain[20];
        bit10_5 = datain[31-1:25];
        bit4_1 = datain[25-1:21];
        bit0 = (0 != 0);
        bit31_11 = 0;
        bit31_12 = 0;
        bit31 = 0;
        bit30_20 = 0;
        bit11_0 = 0;
    end
    else begin
        bit31_11 = 0;
        bit10_5 = 0;
        bit4_1 = 0;
        bit0 = 0;
        bit11 = 0;
        bit31_12 = 0;
        bit31 = 0;
        bit30_20 = 0;
        bit19_12 = 0;
        bit11_0 = 0;
        bit31_20 = 0;
    end
end


always @(bit0, datain, bit19_12, bit11_0, bit10_5, bit31_20, bit31_12, bit4_1, bit31_11, bit11, bit30_20, bit31) begin: CONVINST_CONCATENACION
    if (((datain[7-1:0] == 3) || (datain[7-1:0] == 19) || (datain[7-1:0] == 111))) begin
        dataout = {bit31_11, bit10_5, bit4_1, bit0};
    end
    else if ((datain[7-1:0] == 35)) begin
        dataout = {bit31_11, bit10_5, bit4_1, bit0};
    end
    else if ((datain[7-1:0] == 99)) begin
        dataout = {bit31_12, bit11, bit10_5, bit4_1, bit0};
    end
    else if (((datain[7-1:0] == 55) || (datain[7-1:0] == 23))) begin
        dataout = {bit31, bit30_20, bit19_12, bit11_0};
    end
    else if ((datain[7-1:0] == 103)) begin
        dataout = {bit31_20, bit19_12, bit11, bit10_5, bit4_1, bit0};
    end
    else begin
        dataout = datain;
    end
end

endmodule
