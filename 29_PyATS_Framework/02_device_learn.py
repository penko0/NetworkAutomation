from pyats.topology import loader

''' We use this 'mock' configuration when we do not have real devices but want to perform some tests. We have to download mock.zip from Cisco. '''

tb = loader.load('yaml/my_testbed.yaml')
dev = tb.devices["CSR3"]

dev.connect(log_stdout=False) #In this way we receive only parsed data 

learn_int = dev.learn('interface')
learn_route = dev.learn('static_routing')

print(learn_int.to_dict())