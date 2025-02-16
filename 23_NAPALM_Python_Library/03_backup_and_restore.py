## backup

# from napalm import get_network_driver
#
# driver = get_network_driver('ios')
# device = driver(hostname='192.168.1.23', username='admin', password='admin')
# device.open()
# print("Connected successfully")
# config = device.get_config(retrieve='running')
# run_config = config['running']
# print(run_config)
# with open('bkp.txt', 'w') as conf:
#     conf.write(run_config)
# device.close()
# print("Disconnected from the device")


##########################################################################
''' RESTORE CONFIG'''  #We need to enable "archive" feature on the router (command 'archive path bootflash')

from napalm import get_network_driver

driver = get_network_driver('ios')

device = driver(hostname='192.168.1.23', username='admin', password='admin')
device.open()
print("Connected successfully")

device.load_replace_candidate(filename='bkp.txt')

print(device.compare_config())
if len(device.compare_config()) > 0:
    choice = input("\nWould you like to commit these changes? [yN]: ")
    if choice == 'y':
        print("Committing ....")
        device.commit_config()
    else:
        print("Discarding ...")
        device.discard_config()
else:
    print("No difference")
device.close()
print("Disconnected from the device")