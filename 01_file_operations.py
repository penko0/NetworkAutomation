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
print(dir(file1))
