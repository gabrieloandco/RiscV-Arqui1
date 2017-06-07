// File: PC.v
// Generated by MyHDL 1.0dev
// Date: Tue Nov 29 12:59:40 2016


`timescale 1ns/10ps

module PC (
    datain,
    clk,
    reset,
    enable,
    dataout
);


input [31:0] datain;
input clk;
input reset;
input enable;
output [31:0] dataout;
wire [31:0] dataout;

reg [31:0] register;




assign dataout = register;


always @(posedge clk, posedge reset) begin: PC_WRITE
    if (reset == 1) begin
        register <= 0;
    end
    else begin
        if ((enable == 1)) begin
            register <= datain;
        end
        else if ((reset == 1)) begin
            register <= 0;
        end
        else begin
            register <= register;
        end
    end
end

endmodule