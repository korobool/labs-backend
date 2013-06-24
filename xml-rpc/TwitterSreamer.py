__author__ = 'oleksandr'

import json
import oauth2 as oauth
import urllib2 as urllib
import collections
import pprint
import threading

class Tstream:
    def __init__(self, security_file, mode_debug = 0):
        keys = None
        with open(security_file) as f:
            keys = json.loads(f.read())
        # print keys

        self.oauth_token = oauth.Token( key=keys['access_token_key'],
                                        secret=keys['access_token_secret'])
        self.oauth_consumer = oauth.Consumer(
            key=keys['consumer_key'],
            secret=keys['consumer_secret'])

        self.signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

        self.http_method = "GET"

        self.http_handler  = urllib.HTTPHandler(debuglevel=mode_debug)
        self.https_handler = urllib.HTTPSHandler(debuglevel=mode_debug)


    def twitterreq(self, url, method, parameters):
        req = oauth.Request.from_consumer_and_token(self.oauth_consumer,
                                                 token=self.oauth_token,
                                                 http_method=self.http_method,
                                                 http_url=url,
                                                 parameters=parameters)

        req.sign_request(self.signature_method_hmac_sha1,
                         self.oauth_consumer,
                         self.oauth_token)

        headers = req.to_header()

        if self.http_method == "POST":
            encoded_post_data = req.to_postdata()
        else:
            encoded_post_data = None
            url = req.to_url()

        opener = urllib.OpenerDirector()
        opener.add_handler(self.http_handler)
        opener.add_handler(self.https_handler)

        response = opener.open(url, encoded_post_data)

        return response

    def read(self):
        url = "https://stream.twitter.com/1/statuses/sample.json"
        parameters = []
        response = self.twitterreq(url, "GET", parameters)
        for line in response:
            data = json.loads(line.strip())
            if 'text' in data and 'lang' in data:
                if (data['lang'] == 'en' or data['lang'] == 'ru') and data['coordinates'] != None:
                    yield json.dumps((data['id_str'], data['coordinates']['coordinates'], data['text']))

from xmlrpclib import ServerProxy
twitt_queue = ServerProxy("http://localhost:8002")

def process_twitt(twitt):
    print twitt_queue.add_twitt(twitt), twitt


def run():
    # Create twitter streamer and set credentials
    twitter_stream = Tstream('../../security_keys/skeys.txt')

    # Process twitts one by one
    for twitt in twitter_stream.read():
        process_twitt(twitt)


if __name__ == '__main__':
    run()

