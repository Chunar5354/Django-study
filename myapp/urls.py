from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('book_search', views.book_search, name='book_search'),
	path('movie_search', views.movie_search, name='movie_search'),
]
