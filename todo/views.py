from django.shortcuts import render
from . import models
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
	# Using '-' in order_by() method can order elements in desc order
	todo_items = models.Todo.objects.all().order_by('-added_date')
	content_for_frontend = {
		'todo_items': todo_items,
	}
	return render(request, 'todo/todolist.html', content_for_frontend)

def add_todo(request):
	item = request.POST.get('add_todo')
	# Save item into database
	todo_object = models.Todo.objects.create(text=item)
	length_of_todo = models.Todo.objects.all().count()

	# Redirct current page, the arguement string is the path setting in 
	# (studyapp/urls.py + todo/urls.py)
	# And using a '/' to start from root path
	return HttpResponseRedirect('/todo')

def delete_todo(request, todo_id):
	# Get the id of current todo and delete this todo, notice the path in urls.py
	models.Todo.objects.get(id=todo_id).delete()
	# Redirect is a magic method
	return HttpResponseRedirect('/todo')
