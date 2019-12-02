from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context={
		'Title':'Blog',
		'Heading':'Blog di sini',
	}
	return render(request,'jokowi.html',context)

def recent(request):
	return HttpResponse('RECENT POST')

