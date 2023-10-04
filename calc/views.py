from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def home(request):
	return render(request, "home.html", {'name':'Khusniddin'})


def add(request):
	first=request.POST['first']
	second=request.POST['second']
	s=int(first)+int(second)
	return render(request, 'result.html', {'s':s})