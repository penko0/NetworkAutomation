from pyats.topology import loader

''' We use this 'mock' configuration when we do not have real devices but want to perform some tests. We have to download mock.zip from Cisco. '''
#Seems ospf learn feature does not work on NX-OS as expected
tb = loader.load('mock.yaml')
dev = tb.devices["nx-osv-1"]
dev.connect()

ospf_l = dev.learn('ospf')
print(ospf_l)