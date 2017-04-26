from rest_framework.serializers import ModelSerializer

from musical.models import Genre,Music

class GenreSerializer(ModelSerializer):
	class Meta:
		model=Genre
		fields = ['id','genre','desc','slug']

class MusicSerializer(ModelSerializer):
	class Meta:
		model=Music
		fields = ['id','genre','rating','music_title','slug']



class GenreCreateSerializer(ModelSerializer):
	class Meta:
		model=Genre
		fields = ['genre','desc']


class MusicCreateSerializer(ModelSerializer):
	class Meta:
		model=Music
		fields = ['genre','rating','music_title']