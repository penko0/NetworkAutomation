from pyats.topology import loader
#Please activate the venv first with command: source pyats_venv/bin/activate

tb = loader.load('yaml/my_testbed.yaml')
dev = tb.devices["CSR3"] #Define what device is going to be configured from our my_testbed.yaml file

dev.connect() #Connect to device

pre_learn = dev.learn('static_routing') #Here we learn what are the existing static routes

dev.configure('ip route 1.1.1.110 255.255.255.255 gi1\nip route 1.1.1.111 255.255.255.255 gi1') #Config command that will be executed on the device

post_learn = dev.learn('static_routing') #Here we learn what are the existing static routes

print("\n\n Pre-Learned routes")
print(pre_learn.to_dict()) #Print already existing static routes in dictionary format

print("\n\n Post-Learned routes")
print(post_learn.to_dict()) #Print the static routes after we have applied the new changes

