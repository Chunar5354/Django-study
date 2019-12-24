from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	# This 'add_todo' should as same as it in html-> form-> action
	path('add_todo', views.add_todo, name='add_todo'),
	# This <int:todo_id> comes from todolist.html -> <form action="delete_todo/{{item.id}}>
	# and will send to views.py -> delete(request, todo_id), notice that the name in this file
	# and in views.py must be the same
	path('delete_todo/<int:todo_id>', views.delete_todo, name='delete_todo'),
]

