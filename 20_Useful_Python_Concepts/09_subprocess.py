import subprocess
## subprocess.run()  - Executes commands in shell

# subprocess.run('pwd')
# subprocess.run('ping 8.8.8.8 -c 3', shell=True)
# subprocess.run(['ping' ,'8.8.8.8',  '-c 3'])  #List format, there is no need to specify shell=True

# s1 = subprocess.run('pwd', capture_output=True)

# print(s1)
# print(s1.stdout)

# s2 = subprocess.run('ping 8.8.8.8 -c2', capture_output=True, shell=True, text=True)

# print(s2)
# print(s2.stdout)
# print(s2.stdout.decode()) # We use decode() when we have bytes output. If we have "text=true", we do not use decode()

# s3 = subprocess.run('pwd1', capture_output=True, shell=True, text=True)
# print(s3.stderr)

# ''' with for cycle'''
# s4 = subprocess.run('pwd1', capture_output=True, shell=True, text=True)
# if s4.stdout:
#     print(s4.stdout)
# else:
#     print(s4.stderr)

# ''' The same but we use "returncode() method" '''
# s5 = subprocess.run('pwd', capture_output=True, shell=True, text=True)
# if s5.returncode == 0:
#     print(s5.stdout)
# else:
#     print(s5.stderr)

''' Send output to text file'''
with open('ping.txt', 'w') as ping_file:
    s6 = subprocess.run('ping 8.8.8.8 -c2', shell=True, text=True, stdout=ping_file)