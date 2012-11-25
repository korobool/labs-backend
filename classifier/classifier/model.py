#from cls import Classifier
import cls
import json
import os

def text_processor(text):
    #return str(cls)
    classify = cls.Classifier()
    if not classify.is_already_trained():
        return 'Classifier Is Not Trained Yet'
    genre = classify.document_class(text)
    return genre

def get_known_genres_list():
    data_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]+'/data/'
    genres_string = open(data_dir + 'genre.dat', 'r').read()
    genres = json.loads(genres_string)
    
    return genres
