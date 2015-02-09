from django.shortcuts import render
from main_site.models import Event
from django.http import HttpResponse

def events(request):
	events = Event.objects.all()
	return render(request,'events.html',{

		'events':events,
		



	}) #render

def test(request):
    return render(request,'template_1.html')

