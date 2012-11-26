#from cls import Classifier
import cls
import json
import os

from xmlrpclib import ServerProxy

def text_processor(text):
#    classify = cls.Classifier()
#    if not classify.is_already_trained():
#        return 'Classifier Is Not Trained Yet'
#    genre = classify.document_class(text)
    genre = 'Cannot process request. Service is unreachable.'
    try:
        connect = ServerProxy("http://localhost:8001")
        genre = connect.classify_text(text)
    except Exception as e:
        genre += e
    return genre

def get_known_genres_list():
#    data_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]+'/data/'
#    genres_string = open(data_dir + 'genre.dat', 'r').read()
#    genres = json.loads(genres_string)

    genres = []
    try:
        connect = ServerProxy("http://localhost:8001")
        genres = connect.get_genres_list()
    except Exception as e:
        pass

    return genres
