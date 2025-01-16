from pyats.topology import loader
from genie.conf.base import Interface
#Please activate the venv first with command: source pyats_venv/bin/activate

tb = loader.load('yaml/my_testbed.yaml') #Here we load our configuration file with all devices 
dev = tb.devices["CSR3"] #Define what device is going to be configured from our my_testbed.yaml file
devios = tb.devices["vIOS"]

dev.connect() #Connect to device CSR3
devios.connect() #Connect to device vIOS

csr_int = Interface(device=dev, name="GigabitEthernet2", enabled=True) # enabled = True , this executes "no shutdown" on our interface
vios_int = Interface(device=devios, name="GigabitEthernet0/1")
# print(type(csr_int))
print(dir(csr_int),"\n")

''' CSR config '''
csr_int.ipv4 = '22.3.3.4' #We also can configure the netmask here: '22.3.3.3/24'
csr_int.ipv4.netmask = "255.255.255.0"
#csr_int.ipv4.enable = True #Enable the interface - no shutdown command, but it dos not work on my CSR router


''' vIOS config '''
vios_int.ipv4 = '5.5.5.5/24'
vios_int.ipv4.enable = True #Enable the interface with "no shutdown" command. Does not work on csr100v IOS-XE but works properly on IOSv

# print(type(csr_int.ipv4))
print(dir(csr_int.ipv4)) #Prints the methods available

print(csr_int.build_config(apply=True)) #With apply=false, we do not apply the new configuration
print(vios_int.build_config(apply=True))