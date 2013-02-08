# Create your views here.
from portfolio.models import *
from django.shortcuts import render_to_response
from django.core.mail import send_mail
#send_mail('Django', 'Your PortFolio has been Uploaded.', 'racbhardwaj@gmail.com',
#[''], fail_silently=False)

def webapp (request):
    g = General.objects.all()
    e = Education.objects.all()
    c={'general': g,
       'education':e}
    return render_to_response('result.html', c)


