import datetime

with open('show_commands.txt') as sh_cmd:
    commands = sh_cmd.readlines() #makes a list 
    print(commands)
   
now = datetime.datetime.now().replace(microsecond=0)
for cmd in enumerate(commands, start=1):
    print(cmd[1])
    #print (f"{str(now).replace(' ', ':')}_{str(cmd[0]).zfill(2)}_{cmd[1].replace(' ', '_').strip()}.txt") #Example output file name: 2024-12-19:16:34:03_1_show_running-config.txt
    file_name = f"{str(now).replace(' ', ':')}_{str(cmd[0]).zfill(2)}_{cmd[1].replace(' ', '_').strip()}.txt"
    with open(file_name, 'w') as cmd_data:
         cmd_data.write('test data')