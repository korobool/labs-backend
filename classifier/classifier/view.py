from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from model import text_processor, get_known_genres_list

def home(request):
    genres_line = ''

    for g in get_known_genres_list():
        genres_line += g + ' '

    c = {'genres':genres_line}
    c.update(csrf(request))
    return render_to_response('index.html', c)

def processing(request):
    if request.method == 'POST':
        if request.POST['processing-text'] != u'':
            text = request.POST['processing-text']
	    genre = text_processor(text)
            # genres = get_known_geners_list() 
        else:
            genre = "Empty textarea!"
    else:
        genre = "Sorry, wrong POST request!"
    return render_to_response('processing.html', {'genre':genre})
