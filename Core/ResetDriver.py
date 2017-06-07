from myhdl import block, delay, instance

@block
def ResetDriver(clk,lowTime=20, highTime=5):


	@instance
	def drive_reset():
		while True:
			yield delay(lowTime)
			clk.next=1
			yield delay(highTime)
			clk.next=0

	return drive_reset
