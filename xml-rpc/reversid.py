#!/usr/bin/env python

__author__ = 'Oleksandr Korobov'

import sys

from SimpleXMLRPCServer import SimpleXMLRPCServer

from PyDaemon import Daemon
from reversi_game import ServerClass


class ReversiDaemon(Daemon):
    def run(self):
        while True:
            try:
                server = SimpleXMLRPCServer(("", 8006))
                server.register_instance(ServerClass())
                server.serve_forever()
            except Exception as e:
                pass

if __name__ == "__main__":
    daemon = ReversiDaemon('/tmp/reversi-daemon.pid')
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