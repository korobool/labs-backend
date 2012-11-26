__author__ = 'Oleksandr Korobov'

# XmlRpc client code example

from xmlrpclib import ServerProxy
connect = ServerProxy("http://localhost:8001")
print 'Known genre are:', connect.get_genres_list()
print 'Your genre is: ', connect.classify_text('Put your english text here...')


