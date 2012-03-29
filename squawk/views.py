from models import Squawk
from django.http import HttpResponse
from django.shortcuts import render_to_response

def squawk_list(request):
    return render_to_response(template_name="base.html")