from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	# This 'add_todo' should as same as it in html-> form-> action
	path('movie', views.display, name='movie'),
	# This <int:todo_id> comes from todolist.html -> <form action="delete_todo/{{item.id}}>
	# and will send to views.py -> delete(request, todo_id), notice that the name in this file
	# and in views.py must be the same
]

