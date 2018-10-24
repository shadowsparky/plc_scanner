import client
from pyModbusTCP.client import ModbusClient
		
def findAddresses(unit_id): 
	#for address in range(256): 
	device = client.getClient(unit_id)
	if (device.is_open()): 
		regs = device.read_holding_registers(0,125)
		if (regs): 
			print(regs)
		else: 
			print("Error on reading registers...")
	else: 
		print("CLIENT IS NOT OPEN")
		
findAddresses(77)