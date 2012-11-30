import os
import datetime
from django.shortcuts import render_to_response, HttpResponse
from django.core.context_processors import csrf
from model import text_processor, get_known_genres_list
import smtplib

#def mail(msg):
#    try:
#        fromaddr = 'oleksandr.korobov@gmail.com'
#        toaddrs  = 'oleksandr.korobov@gmail.com'
#        # msg = 'Message'
#
#        # Credentials (if needed)
#        username = 'oleksandr.korobov@gmail.com'
#        password = 'grammarly.c0m'
#
#        # The actual mail send
#        server = smtplib.SMTP('smtp.gmail.com:587')
#        server.starttls()
#        server.login(username,password)
#        server.sendmail(fromaddr, toaddrs, msg)
#        server.quit()
#    except:
#        pass

def save(msg):
    try:
        time = datetime.datetime.now()
        session_dir = os.path.split(os.path.split(os.path.split(
                        os.path.abspath(__file__))[0])[0])[0]+'/data/sessions/'
        with open(session_dir + str(time) + '.txt', 'w') as file:
            file.write(msg.encode('utf-8'))
        return ''
    except: # Exception as e:
        return 'Some errors occurred.'

def home(request):
    return render_to_response('home.html')

def classifier(request):
    genres_line = ''

    for g in get_known_genres_list():
        genres_line += g + ' '

    c = {'genres':genres_line}
    c.update(csrf(request))
    return render_to_response('classifier.html', c)

def processing(request):
    comment = ''
    if request.method == 'POST':
        if request.POST['processing-text'] != u'':
            text = request.POST['processing-text']
            genre = text_processor(text)
            comment = save('________________________\n'
                           + genre +
                           '\n________________________\n\n\n\n' + text)
        else:
            genre = "Empty textarea!"
    else:
        genre = "Sorry, wrong POST request!"
    return HttpResponse(genre)
