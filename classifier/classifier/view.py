from django.shortcuts import render_to_response
from django.core.context_processors import csrf

def home(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('index.html', c)

def processing(request):
    if request.method == 'POST':
        if request.POST['processing-text'] != u'':
            genre = request.POST['processing-text'] 
        else:
            genre = "Empty textarea!"
    else:
        genre = "Sorry, wrong POST request!"
    return render_to_response('processing.html', {'genre':genre})