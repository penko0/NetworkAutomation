from pyats.topology import loader



''' We use this 'mock' configuration when we do not have real devices but want to perform some tests. We have to download mock.zip from Cisco.  '''


tb = loader.load('mock.yaml')
dev = tb.devices["nx-osv-1"]
dev.connect()


p1= dev.parse("show inventory")
print(p1)
print('My serial for slot1 is: ' + p1['name']['Slot 1']['serial_number'])
