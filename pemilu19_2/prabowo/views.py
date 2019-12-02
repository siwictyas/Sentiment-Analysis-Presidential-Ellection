from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request,'prabowo.html')

def recent(request):
	return HttpResponse('RECENT POST')

