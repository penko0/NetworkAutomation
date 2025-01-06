import os

# print(f"Current dir is {os.getcwd()}")
# os.chdir('../Docker')
# print(f"Dir changed to {os.getcwd()}")
# print(os.listdir())
# print(f"The number of files and folders is {len(os.listdir())}")
# print(os.system('ls -larth')) #Execute a command on our operating system

# files = (os.listdir())
# files.sort() #Sorts the file names 
# for file in files:
#     print(file)

#How to open/print a file

file1 = open('config1.txt', 'r')
#print(dir(file1)) #With dir we print the methods available for that file. In order to read the file we use "read" method.

#print(file1.read()) #Read method reads the whole file
#print(file1.readlines()) #Prints the content in a list format.

# commands = file1.readlines()
# for command in commands:
#     print(command.rstrip('\n'))
file1.close()  #Always use .close() method because without it , the file will stay open in the memory
################
'''with open method'''
# with open('config1.txt') as file1:
#     print(file1.readlines())

################
'''writing content to a file'''

with open('config2.txt', 'w') as file2:
    file2.write("testdata\n")

#Append data without overwriting the file

# with open('config2.txt', 'a') as file2:
#     file2.write("testdata12")

#Create new file with name "new_file.txt" and add some text to it:
with open('new_file.txt', 'w') as dest_file:
    dest_file.write('some text')

#How to remove a file
os.remove('new_file.txt')