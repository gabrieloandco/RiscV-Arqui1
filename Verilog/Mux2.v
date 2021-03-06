// File: Mux2.v
// Generated by MyHDL 1.0dev
// Date: Tue Nov 29 12:59:58 2016


`timescale 1ns/10ps

module Mux2 (
    ALUsrc,
    in1_Mux2,
    in2_Mux2,
    output_Mux2
);


input [0:0] ALUsrc;
input [31:0] in1_Mux2;
input [31:0] in2_Mux2;
output [31:0] output_Mux2;
reg [31:0] output_Mux2;




always @(in1_Mux2, in2_Mux2, ALUsrc) begin: MUX2_BEHAVIOR_MUX2
    if ((ALUsrc == 0)) begin
        output_Mux2 = in1_Mux2;
    end
    else begin
        output_Mux2 = in2_Mux2;
    end
end

endmodule
