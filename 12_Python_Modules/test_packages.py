from myconflib import cisco_cmd_executor, users_cmd_gen, user_cmd_gen

user_cmd = user_cmd_gen('test_admin1', 15)
# print(user_cmd)

#List with user details
users_details = [{'name': 'user1', 'priv': 15},
                  {'name': 'user2', 'priv': 15},
                  {'name': 'user3', 'priv': 1}]

users_cmd = users_cmd_gen(*users_details)
# print(users_cmd)

#Dictionary with login details that we pass to function cisco_cmd_executor() 
lab_csr1 = {'hostname': '192.168.1.23',  #Dictionary that we pass as an argument to to function cisco_cmd_executor 
            'commands': users_cmd,
            'username': 'admin',
            'password': 'admin'}
# cisco_cmd_executor(hostname='192.168.0.63',
#                    commands=users_cmd,
#                    username='admin',
#                    password='admin')

cisco_cmd_executor(**lab_csr1)  # '**' means dictionary , '*' means list

