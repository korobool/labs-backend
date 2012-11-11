__author__ = 'Oleksandr Korobov'
from xmlrpclib import ServerProxy
connect = ServerProxy("http://korobov-labs.com:8000")
print connect.system.listMethods()
key = connect.login('She was in love but he has killed her. After this murder he was arrested.')
print key
