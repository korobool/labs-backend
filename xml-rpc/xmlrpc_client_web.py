__author__ = 'Alien'
from xmlrpclib import ServerProxy
connect = ServerProxy("http://service.korobov-labs.com:8000")

print connect.system.listMethods()
key = connect.login("root", "xn3ma8")
print connect.add_num(key, 5, 10)
print connect.add_str(key, 5, 10)
raw_input()
