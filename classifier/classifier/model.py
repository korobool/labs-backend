from xmlrpclib import ServerProxy

def text_processor(text):
    genre = 'Cannot process request. Service is unreachable.'
    try:
        connect = ServerProxy("http://54.214.233.91:8001")
        genre = connect.classify_text(text)
    except Exception as e:
        genre += e
    return genre

def get_known_genres_list():
    genres = []
    try:
        connect = ServerProxy("http://54.214.233.91:8001")
        genres = connect.get_genres_list()
    except Exception as e:
        pass

    return genres

from twitter_live import fetchsamples

def fetch_samples(id):
    messages = fetchsamples(id=id)
    return messages
    
