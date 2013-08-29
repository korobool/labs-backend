#!/usr/bin/env python

__author__ = 'Oleksandr Korobov'

import sys

from PyDaemon import Daemon

from SimpleXMLRPCServer import SimpleXMLRPCServer
import cls

class ServerClass():
    def __init__(self):
        self.ai_agent = cls.Classifier()
    def classify_text(self, text):
        genre = self.ai_agent.document_class(text)
        return genre
    def get_genres_list(self):
        return self.ai_agent.genres

class ClassifierDaemon(Daemon):
    def run(self):
        while True:
            try:
                server = SimpleXMLRPCServer(("", 8001))
                server.register_instance(ServerClass())
                server.register_introspection_functions()
                server.serve_forever()
            except Exception as e:
                pass

if __name__ == "__main__":
    daemon = ClassifierDaemon('/tmp/classifier-daemon.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)