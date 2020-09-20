from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail

from .form_s import UserLoginForm, UserRegisterForm


def user_login(request):
	if request.method == 'POST':
		user_login_form = UserLoginForm(data=request.POST)
		if user_login_form.is_valid():
			data = user_login_form.cleaned_data

			user = authenticate(username=data['username'], password=data['password'])

			if user:
				login(request, user)
				# return redirect('article: article_list')
				return HttpResponseRedirect('/')
			else:
				return HttpResponse('current user not exists')

		else:
			return HttpResponse('unvalid input')

	elif request.method == 'GET':
		user_login_form = UserLoginForm()
		context = {'form': user_login_form}
		return render(request, 'userprofile/login.html', context)
	
	else:
		return HttpResponse('please use POST or GET method')

def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

def user_register(request):
	if request.method == 'POST':
		user_register_form = UserRegisterForm(data=request.POST)
		if user_register_form.is_valid():
			data = user_register_form.cleaned_data
			new_user = User.objects.create_user(username=data['username'],email=data['email'],password=data['password'])
			
			# login and eturn to todolist page
			login(request, new_user)
			return HttpResponseRedirect('/')
		else:
			return HttpResponse('something wrong with register form')

	elif request.method == 'GET':
		user_register_form = UserRegisterForm()
		context = {'form': user_register_form}
		return render(request, 'userprofile/register.html', context)
	else:
		return HttpResponse('please use GET or POST method')


def mail_send(request):
	send_mail(
		'Chunar sends you a message.',
		'hellow man',
		'1186330927@qq.com',
		['1484958755@qq.com'],
		fail_silently = False,
	)
	return HttpResponse('Successfully sended')
# Create your views here.
