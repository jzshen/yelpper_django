from django.shortcuts import render
from django.template import Context, loader, Template

# Create your views here.

from django.http import HttpResponse
from yelpper_django_app.request import RequestForm

def index(request):
	t = Template("my name is {{ my_name }}")
	c = Context({"my_name": "test"})
	#t = loader.get_template('template/yelpper_django_app/index.html')
	#c = Context("")
 	return HttpResponse(t.render(c))

def request(request):
	if request.method == 'GET':
		form = RequestForm()
	elif request.method == 'POST': # If the form has been submitted...
		form = ReqestForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
        	distance = form.cleaned_data['distance'] 
    		prices = form.cleaned_data['prices']
    		uberType = form.cleaned_data['sender']
	else:
		form = RequestForm() # An unbound form

	return render(request, 'index.html', {
        'form': form
    })



