# Created 7/14/2022
# ZtM course Decorators practice

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:

from time import time

user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def check_valid(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
        else:
            return print("User not valid")
    return check_valid


@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)