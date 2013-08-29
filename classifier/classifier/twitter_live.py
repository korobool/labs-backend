# -*- coding: utf-8 -*-
from xmlrpclib import ServerProxy
import json
twitt_queue = ServerProxy("http://ai-labs.org:8002")

def fetchsamples(id='0'):
    import time;time.sleep(0.33);
    data = json.loads(twitt_queue.get_twitts_list(id))
    for item in data:
        item['text'] = item['text']
    return data
