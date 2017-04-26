from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView
from musical.models import Music,Genre
from musical.api.serializers import (GenreSerializer,
	MusicSerializer,
	GenreCreateSerializer,
	MusicCreateSerializer
	)


class GenreListAPI(ListAPIView):
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer

class GenreDetailAPI(RetrieveAPIView):
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer

class GenreUpdateAPI(UpdateAPIView):
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer

class GenreCreateAPI(CreateAPIView):
	queryset = Genre.objects.all()
	serializer_class = GenreCreateSerializer


class GenreDestroyAPI(DestroyAPIView):
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer

class MusicListAPI(ListAPIView):
	queryset = Music.objects.all()
	serializer_class = MusicSerializer

class MusicDetailAPI(RetrieveAPIView):
	queryset = Music.objects.all()
	serializer_class = MusicSerializer

class MusicUpdateAPI(UpdateAPIView):
	queryset = Music.objects.all()
	serializer_class = MusicSerializer


class MusicDestroyAPI(DestroyAPIView):
	queryset = Music.objects.all()
	serializer_class = MusicSerializer

class MusicCreateAPI(CreateAPIView):
	queryset = Genre.objects.all()
	serializer_class = MusicCreateSerializer