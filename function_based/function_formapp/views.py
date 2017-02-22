from django.shortcuts import render

# Create your views here.
from .models import Contact
from .forms import ContactForm

def blog_post(request):
	template_name = 'form.html'
	if request.method =='POST':
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