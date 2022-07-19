# Created 7/19/2022

import requests

# url = 'https://api.pwnedpasswords.com/range' + 'password123'
# res = requests.get(url)
# print(res) # this gives us a response of 404, which is not good.

# let us try a hashed password. This is how they check the password in the database it would be easy to compromise our passwords if they were stored unencrypted
url = 'https://api.pwnedpasswords.com/range' + 'CBFDA'
res = requests.get(url)
print(res) # we still get error 404. 