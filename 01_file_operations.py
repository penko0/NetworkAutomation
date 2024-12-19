import os
print(f"Current dir is {os.getcwd()}")
os.chdir('Docker')
print(f"Dir changed to {os.getcwd()}")
print(os.listdir())
print(len(os.listdir()))