import sys
#print(sys.path) #Print the system path for python
sys.path.append('/home/pen/NetworkAutomation/11_Python_Functions') #In order to open a module function from different dir, we must import the dir to the function/module

from password_gen import user_cmd_gen

print(user_cmd_gen('admin', 15))