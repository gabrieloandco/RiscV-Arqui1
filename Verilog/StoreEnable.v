// File: StoreEnable.v
// Generated by MyHDL 1.0dev
// Date: Sun Oct 30 17:56:04 2016


`timescale 1ns/10ps

module StoreEnable (
    DWidth,
    Datain,
    Store_E
);


input [2:0] DWidth;
input [1:0] Datain;
output [3:0] Store_E;
reg [3:0] Store_E;



// Datain son los 2 bits menos significativos de la salida de la ALU.
// A continuacion una tabla indicando todas las posibles combinaciones del ultimo numero 
// hexadecimal de la direccion a la RAM en bits, y para cada uno de ellos la salida sera un enabler de escritura
// de la RAM (enabler de escritura por byte).
always @(DWidth, Datain) begin: STOREENABLE_SELECTOR
    if (((DWidth == 0) || (DWidth == 3))) begin
        case (Datain)
            'h0: begin
                Store_E = 1;
            end
            'h1: begin
                Store_E = 2;
            end
            'h2: begin
                Store_E = 4;
            end
            'h3: begin
                Store_E = 8;
            end
            default: begin
                Store_E = 0;
            end
        endcase
    end
    else if (((DWidth == 1) || (DWidth == 4))) begin
        if (((Datain == 0) || (Datain == 1))) begin
            Store_E = 3;
        end
        if (((Datain == 2) || (Datain == 3))) begin
            Store_E = 12;
        end
        else begin
            Store_E = 0;
        end
    end
    else if ((DWidth == 2)) begin
        Store_E = 15;
    end
    else begin
        Store_E = 0;
    end
end

endmodule
