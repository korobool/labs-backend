__author__ = 'Oleksandr Korobov'

from xmlrpclib import ServerProxy

connect = ServerProxy("http://localhost:8001")

print connect.system.listMethods()

genre = connect.classify_text('She was in love but he has killed her. After this murder he was arrested.')

print genre
