from django.db import models

# Create your models here.
class BookSearch(models.Model):
	search = models.CharField(max_length=500)
	created = models.DateTimeField(auto_now=True)

	def __str__(self):
		# This can show the name of search if admin page, not just 'Search object'
		return '{}'.format(self.search)

	class Meta():
		# This can change the displayed 'Searchs' into 'Searches'
		# Because django automaticlly add a 's' at the end of class-name
		verbose_name_plural = 'Book Searches'

class MovieSearch(models.Model):
	search = models.CharField(max_length=500)
	created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{}'.format(self.search)

	class Meta():
		verbose_name_plural = 'Moive Searches'
