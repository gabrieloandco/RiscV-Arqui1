from myhdl import *
from <NombredelModulo> import *
import random
def tb<NombredelModulo>():
	
#definición del TestBench de un módulo

# Se definen las señales de entrada y salida

	señalentrada1 = Signal(modbv(0)[tamaño:]) 
	señalentrada2 = Signal(modbv(0)[tamaño:])
	señalentrada3 = Signal(modbv(0)[tamaño:])
	#........................
	señalentradaN = Signal(modbv(0)[tamaño:])
    	
	señaldesalida1 =  Signal(modbv(0)[tamaño:])
	señaldesalida2 =  Signal(modbv(0)[tamaño:])
	#.........................
	señaldesalidaN =  Signal(modbv(0)[tamaño:])
 
#Se coloca “signal” para definir los puertos de entrada y de salida de las señales del módulo
# Con el “modbv” defines un entero (con un tamaño dado) que varía y puede sumarse y multiplicarse, a diferencia de su primo “intbv”
	
	dut = <NombredeLaFuncion>(datain,dataout)
	interv = delay(7)

# mediante el “interv = delay(n)” se generan n cantidad de conteos de tiempo determinados y se asignan a una variable “interv”

	@always(interv)
	def stim(): 	

#se hace el estímulo a la simulación 
       
		datain.next = random.randint(0, 2**tamaño)
		señalentrad1.next = random.randint(0, 2**tamaño)
		señalentrada2.next = random.randint(0, 2**tamaño)
		señalentrada3.next = random.randint(0, 2**tamaño)
		#...............
         	señalentradaN.next = random.randint(0, 2**tamaño)

#mediante el “random.randint()” se generan entradas aleatorias en un rango de valores especificados en el argumento de la función. 

    		return dut, stim

def simulation():
	signals = traceSignals(tb<NombredelModulo>)
	sim = Simulation(signals)
	sim.run(500)

# “traceSignals()” habilita el rastreo de la señal en un archivo VCD para la visualización de forma de onda

simulation()

def convert()
	señal1=Signal(modbv(0)[tamaño:])
	señal2=Signal(modbv(0)[tamaño:])
	#......
	señaln=Signal(modbv(0)[tamaño:])
	ToVerilog(nombrefuncion,señal1,señal2,señal)
convert()
