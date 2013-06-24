# -*- coding: utf-8 -*- #
import oauth2 as oauth
import urllib2 as urllib
import json

access_token_key = "135171548-zwm1qakSOKz7STOryxfhWji1pJDIZ2xRyzO7h3f7"
access_token_secret = "PDj7kl31DBmspnWdL8NvMwmIDpDGUXfj4knDl8QQ"

consumer_key = "pG4tFgUEuMlERIZl3553ag"
consumer_secret = "BiUwAJUfRpD4DBVz8A71LiQ8Aoj87ok6RMb5EYQ7ao4"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"

http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''

def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  # url = "https://stream.twitter.com/1/statuses/sample.json"
  # parameters = []
  # messages = []
  # response = twitterreq(url, "GET", parameters)
  # for line in response:
  #   data = json.loads(line.strip())
  #   if 'text' in data and 'lang' in data:
  #       if (data['lang'] == 'en' or data['lang'] == 'ru') and data['coordinates'] != None:
  #           if len(messages) < 1:
  #             print json.dumps({'coordinates':data['coordinates']['coordinates'], 'text':data['text']})
  #             message = json.dumps({'coordinates':data['coordinates']['coordinates'], 'text':data['text']})
  #             messages.append(message)
  #           else:
  #             return messages
  import time
  import random
  time.sleep(2)
  return [json.dumps({"text": random.choice(messages),
                      "coordinates": [random.random()*90, random.random()*90]})
         ]

# if __name__ == '__main__':
#   fetchsamples()
messages = [
  ["Just posted a video @ Little Miami http://t.co/LaqYwuRlWP"],
  ["Imaginanse comerse ese #M&amp;M #fun #chocolate @ Times Square http://t.co/n4HZVgfJoo"],
  ["Need mates that want to go races"],
  ["I love you. Just more you know."],
  ["@melodisurmeli (@ Big Mamma's w/ 4 others) http://t.co/VKrUycUgc6"],
  ["RESPECT!"],
  ["I wish church was outside today! #sundaysun"],
  ["Stuck in d worst traffic jam here in #Agra. Apprntly,1 of d gates fr rail crossing not working!#Traffucked!"],
  ["Really want to change my hair colour to something lighter for the summer #summer"],
  ["5 minutes left. #LM24 \ud83d\ude0b\ud83d\ude04"],
  ["@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@WWWWWWWWWWWWWWWWWWWWWWWWWW"],
  ["MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"]
  ]