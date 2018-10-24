from pyModbusTCP.client import ModbusClient

def getClient(unit_id): 
	client = ModbusClient()
	client.host("127.0.0.1")
	client.port(502)
	client.timeout(0.1)
	client.unit_id(unit_id)
	client.open()
	return client