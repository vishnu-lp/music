from django import forms
from .models import Genre,Music



class GenreForm(forms.ModelForm):
	class Meta:
		model = Genre
		fields = ['genre','desc']

class MusicForm(forms.ModelForm):
	class Meta:
		model = Music
		fields = ['music_title','rating','genre']

	
