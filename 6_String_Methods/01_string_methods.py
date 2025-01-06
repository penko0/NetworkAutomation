username='admin'

print(username.upper())

print(username.capitalize()) #Capitalizes only the first letter


ip = '192.168.1.1'
device = 'router'
print(f"IP address is {ip}\nDevice type is {device}")


# How to find index number of given string. The index starts from 0
print(username.find('n')) 

#How to check if a value is a number
a_number = '\u0035' #ASCII format
print(f"Is it a number/digit: {a_number.isdigit()}")
print(f"Is it ascii: {a_number.isascii()}")

b_letter = 'A'
print(f"Is it ascii: {b_letter.isascii()}")

'''Is this an identifier? Should not start with nummber! allowed characters: a-z, A-Z ,0-9, _'''
an_identifier = 'A123a_'
print(f"Is it identifier: {an_identifier.isidentifier()}")

'''Is it printable'''
printable="Hi there"
print(f"Is it printable: {printable.isprintable()}")

# How to use 'join' to connect words from given list
list1 = ['Cisco', 'IOS', '17.3']
print('-'.join(list1))
print('.'.join(list1))

'''ljust'''
print('abc'.ljust(18), '12345')
print('abasdsadasc'.ljust(18), '12345')
print('adsadadsssssaabc'.ljust(18), '12345')

'''maketrans'''
message = "Hey there..."
trans = message.maketrans('e', 'E')
print(message.translate(trans))

'''partition'''
message = "ip route 192.168.0.0"
print(message.partition("route"))

'''replace'''
message = "Hello there"
print(message.replace("there","world")) 

'''split'''
users = 'user1, user2, user3'
user_list = users.split(', ')
print(users)
print(user_list)
for user in user_list:
    print(f"The username is: {user}")

'''splitlines'''  #This method will produce a list
print("user1\nuser2\nuser3".splitlines())
print("user1 ,user2, user3".splitlines())

'''translate'''  #Translates one ASCII character to another. See the ASCII character table for more info
trans = {46: 33} 
print("Hey there...".translate(trans))

'''zfill'''

print('122'.zfill(5)) #Adds additional zeroes in order to create a string with 5 characters, if we need 