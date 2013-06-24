#!/usr/bin/env python

__author__ = 'Oleksandr Korobov'

import sys

from PyDaemon import Daemon
from TwitterQueue import TwitterQueue

from SimpleXMLRPCServer import SimpleXMLRPCServer


class TwitterQueueServerClass():
    def __init__(self):
        self.twitter_queue = TwitterQueue()

    def add_twitt(self, twitt):
        self.twitter_queue.add(twitt)
        print twitt
        return True

    def get_twitts_list(self, id=0):
        return self.twitter_queue.get_twitts(id)

class TwitterQueueDaemon(Daemon):
    def run(self):
        while True:
            try:
                server = SimpleXMLRPCServer(("", 8002))
                server.register_instance(TwitterQueueServerClass())
                server.register_introspection_functions()
                server.serve_forever()
            except Exception as e:
                pass

if __name__ == "__main__":
    daemon = TwitterQueueDaemon('/tmp/twitter-queue-daemon.pid')
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