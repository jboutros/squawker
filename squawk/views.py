from models import Squawk
from django.http import HttpResponse
from django.template.context import RequestContext
from django.shortcuts import render_to_response

def squawk_list(request):
    squawks = Squawk.objects.all()
    c= {}
    c['squawks'] = squawks
    return render_to_response("home.html", c, context_instance=RequestContext(request))