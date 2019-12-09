from django.shortcuts import render
from bs4 import BeautifulSoup
import requests


def home(request):
	return render(request, 'base.html')

def new_search(request):
	# search is what users type in the input line
	search = request.POST.get('search')  # The 'search' should be as same as 'name' property in html
	stuff_for_frontend = {
		'search': search,
	}
	return render(request, 'myapp/new_search.html', stuff_for_frontend)

# Create your views here.
