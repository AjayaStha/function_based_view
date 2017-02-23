from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.http import HttpResponse

# Create your views here.


def blog_post(request): 
	template_name = 'form.html'
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Thank you')
	else:
		form = ContactForm()
	context = {
		'form':form

		}
	return render(request,template_name,context)