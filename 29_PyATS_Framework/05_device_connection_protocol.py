from pyats.topology import loader

#Please activate the venv first with command: source pyats_venv/bin/activate

tb = loader.load('yaml/my_testbed.yaml') #Here we load our configuration file with all devices 
dev = tb.devices["vIOS"] #Define what device is going to be configured from our my_testbed.yaml file

''' Here we just use to methods to execute commands, telnet and ssh '''

print("Telnet Connection")
dev.connect(alias='telnet', via='telnet', log_stdout=False)  #Connect to device via Telnet
print(dev.telnet.execute("show users"))

print("SSH Connection","\n\n")
dev.connect(alias='ssh', via='cli', log_stdout=False) #Connect to device via SSH

print(dev.ssh.execute("show version"))