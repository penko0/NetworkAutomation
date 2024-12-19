import os
print(f"Current dir is {os.getcwd()}")
os.chdir('../Docker')
print(f"Dir changed to {os.getcwd()}")
print(os.listdir())
print(f"The number of files and folders is {len(os.listdir())}")
print(os.system('ls -larth'))

files = (os.listdir())
files.sort() #Sorts the file names 
for file in files:
    print(file)