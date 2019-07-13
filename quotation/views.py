from django.shortcuts import render
from django.http import *
from .models import Quote
from .forms import *

def index(request):
	return HttpResponse("<h1>Quote Index</h1>")


def quoteout(request):
	obj = Quote.objects.all()
	return render(request, 'quotation/quoteout.html', {'obj':obj})

def quotein(request):
	if request.method == 'POST':
		form = quote_form(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/quoteinput/')

	else:
		form = quote_form()

	return render(request, 'quotation/quotein.html', {'form':form})