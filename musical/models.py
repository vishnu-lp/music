from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.:

class Genre(models.Model):
	genre = models.CharField(max_length=50,db_index=True)
	slug = models.SlugField(max_length=20)
	desc = models.TextField(max_length=100,db_index=True,blank=True)

	def __str__(self):
		return self.genre





class Music(models.Model):
	music_title = models.CharField(max_length=50)
	rating = models.IntegerField(db_index=True)
	genre = models.ForeignKey(Genre)
	slug = models.SlugField(db_index=True)
	
	def __str__(self):
		return self.music_title	 	
		

