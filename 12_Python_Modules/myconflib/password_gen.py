import string
import random

def user_cmd_gen(user, priv):
    password = ''.join(random.choices(string.ascii_uppercase +
                                      string.digits +
                                      string.ascii_lowercase, k=8))
    conf_list = [f"username {user} privilege {priv} secret {password}"]
    return conf_list


def users_cmd_gen(*args):
    cmd_list = []
    for user in args:
        password = ''.join(random.choices(string.ascii_uppercase +
                                          string.digits +
                                          string.ascii_lowercase, k=8))
        user_cmd = f"username {user['name']} privilege {user['priv']} secret {password}"
        cmd_list.append(user_cmd)
    return cmd_list

if __name__ == '__main__': #This will be executed only if we run the function locally. If we have executed this function as imported function from another file like in test_packages.py , the commands bellow will not execute
    print(__name__)
    user_cmd1 = user_cmd_gen('test_admin', 15)
    print(user_cmd1)


