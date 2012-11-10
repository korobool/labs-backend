#from cls import Classifier
import cls
import json

def text_processor(text):
    #return str(cls)
    classify = cls.Classifier()
    if not classify.is_already_trained():
        return 'Classifier Is Not Trained Yet'
    genre = classify.document_class(text)
    return genre

def get_known_genres_list():
    genres_string = open('/home/ubuntu/production/labs-backend/classifier/classifier/genre.dat', 'r').read()
    genres = json.loads(genres_string)
    
    return genres
