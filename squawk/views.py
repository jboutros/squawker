from models import Squawk
from forms import AddSquawkForm
from django.http import HttpResponse
from django.template.context import RequestContext
from django.shortcuts import render_to_response

def squawk_list(request):
    if request.method == "POST":
        add_form = AddSquawkForm(request.POST)
        if add_form.is_valid():
            s = Squawk()
            s.text = add_form.cleaned_data['squawk']
            s.user = request.user
            s.save()
    form = AddSquawkForm()
    squawks = Squawk.objects.all().order_by('-id')
    c= {}
    c['squawks'] = squawks
    c['form'] = form
    return render_to_response("home.html", c, context_instance=RequestContext(request))