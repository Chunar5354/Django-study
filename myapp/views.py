from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
from . import models

BASE_URL = 'http://search.dangdang.com/?key={}&act=input'


def home(request):
	return render(request, 'base.html')

def new_search(request):
	# search is what users type in the input line
	search = request.POST.get('search')  # The 'search' should be as same as 'name' property in html
	# Create a new elemet in database
	models.Search.objects.create(search=search)
	# quote_plus can automaticly add a '+' to replace tthw whitespaces
	final_url = BASE_URL.format(quote_plus(search))
	# Something like spider
	response = requests.get(final_url)
	response.encoding = 'gb2312'
	data = response.text
	soup = BeautifulSoup(data, 'html.parser')
	book_list = soup.find('ul', {'class': 'bigimg'}).find_all('li')

	all_books = []
	for book in book_list:
		book_title = book.a.get('title')
		book_url = book.a.get('href')
		book_img = book.a.img.get('data-original')
		if not book_img:
			book_img = book.a.img.get('src')
		book_price = book.find('span', {'class': 'search_now_price'}).text
		
		book_info = [book_title, book_url, book_img, book_price]
		all_books.append(book_info)

	# After you add things to show in this dictionary, you need to add them in html files
	stuff_for_frontend = {
		'search': search,
		'books_list': all_books,
	}
	return render(request, 'myapp/new_search.html', stuff_for_frontend)

# Create your views here.
