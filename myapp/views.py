from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
import re
from . import models


def home(request):
	return render(request, 'base.html')

def book_search(request):
	BASE_URL = 'http://search.dangdang.com/?key={}&act=input'
	# search is what users type in the input line
	try:
		search = request.POST.get('search')  # The 'search' should be as same as 'name' property in html
		# Create a new elemet in database
		models.BookSearch.objects.create(search=search)
		# quote_plus can automaticly add a '+' to replace the whitespaces
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
	except:
		search = None
		all_books = []

	# After you add things to show in this dictionary, you need to add them in html files
	stuff_for_frontend = {
		'search': search,
		'books_list': all_books,
	}
	return render(request, 'myapp/book_search.html', stuff_for_frontend)

def movie_search(request):
	BASE_URL = 'https://search.bilibili.com/all?keyword={}&from_source=nav_search_new'
	try:
		search = request.POST.get('search')
		models.MovieSearch.objects.create(search=search)
		final_url = BASE_URL.format(quote_plus(search))

		headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
		           'Cookie': "_uuid=2BF1AD87-ABC1-13D1-7057-2E4A480A846095922infoc; buvid3=D58FA21E-6D87-47D9-A1F8-0B28C7A6FDF9190950infoc; LIVE_BUVID=AUTO4115675688967302; sid=i9lpnyn8; UM_distinctid=16d2805152b26-01ae43b21ea88-5f4e2917-144000-16d2805152c27; im_notify_type_36083852=0; CURRENT_FNVAL=16; stardustvideo=1; rpdid=|(JY))R~kJl)0J'ulY)~kYkm); arrange=matrix; INTVER=1"}
		response = requests.get(final_url, headers=headers)
		response.encoding = 'utf-8'
		data = response.text
		soup = BeautifulSoup(data, 'html.parser')
		movie_list = soup.find_all('li', {'class': 'video-item matrix'})

		all_movies = []
		for movie in movie_list:
			title = movie.a.get('title')
			href = movie.a.get('href')
			watch_times = re.sub('\s', '', movie.find('span', {'title': '观看'}).text)
			upload_time = re.sub('\s', '', movie.find('span', {'title': '上传时间'}).text)

			movie_info = [title, href, watch_times, upload_time]
			all_movies.append(movie_info)

	except:
		search = None
		all_movies = []

	stuff_for_frontend = {
		'search': search,
		'movies_list': all_movies,
	}
	return render(request, 'myapp/movie_search.html', stuff_for_frontend)

# Create your views here.
