__author__ = 'oleksandr'

import collections

class TwitterQueue():

    def __init__(self):
        self.twitter_queue = collections.deque()

    def get_twitts(self, id):
        return filter(
            lambda twitt: twitt['id_str'] > id, self.twitter_queue)

    def add(self, twitt):
        self.twitter_queue.append(twitt)
        if len(self.twitter_queue) > 10:
            self.twitter_queue.popleft()
        return True