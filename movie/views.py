from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings


def index(request):
	return render(request, 'movie/index.html')

def display(request):
	video_url = 'BENEE-Glitter.mp4'

	return render(request, 'movie/video.html', {'url':video_url})


# Create your views here.
