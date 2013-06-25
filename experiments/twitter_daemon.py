__author__ = 'Oleksandr Korobov'

import collections
import pprint
import threading

import TwitterSreamer

twitts = collections.deque()

# Create twitter streamer an set credentials
twitter_stream = TwitterSreamer.Tstream('../../security_keys/skeys.txt')

queue_lock = threading.Lock()

def process_twitt(twitt):
    with queue_lock:
        twitts.append(twitt)
        if len(twitts) > 10:
            twitts.popleft()
        print twitts

    print twitts

for twitt in twitter_stream.read():
    process_twitt(twitt)

