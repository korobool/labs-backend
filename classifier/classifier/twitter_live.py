from xmlrpclib import ServerProxy
import json
twitt_queue = ServerProxy("http://localhost:8002")

def fetchsamples(id='0'):
    return json.loads(twitt_queue.get_twitts_list(id))