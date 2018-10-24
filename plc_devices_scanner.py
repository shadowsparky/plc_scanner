import client
from pyModbusTCP.client import ModbusClient

def findDevices(): 
	founded_devices = 0 
	success_addresses = ""
	for unit_id in range(256):
		device = client.getClient(unit_id)
		if (device.is_open()): 
			regs = device.read_holding_registers(0,2)
			if (regs): 
				print(str(unit_id) + " SUCCESS " + str(regs))
				success_addresses += " " + str(unit_id)
				founded_devices += 1
			else:
				print(str(unit_id) + " device not found")
		else: 
			print("CLIENT IS NOT OPEN")
			return
		
	if (founded_devices != 0): 
		print("DEVICE FOUNDED " + str(founded_devices))
		print("DEVICE IDS" + str(success_addresses))
		
findDevices()