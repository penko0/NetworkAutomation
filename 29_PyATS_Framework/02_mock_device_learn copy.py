from pyats.topology import loader

''' We use this 'mock' configuration when we do not have real devices but want to perform some tests. We have to download mock.zip from Cisco. '''

tb = loader.load('yaml/my_testbed.yaml')
dev = tb.devices["CSR3"]
dev.connect()

ospf_l = dev.learn('ospf')
print(ospf_l)