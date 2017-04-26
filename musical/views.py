from django.shortcuts import get_object_or_404,render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from .models import Genre,Music
from .forms import GenreForm,MusicForm
from django.contrib import messages


def genre_create(request):
	form = GenreForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"succesfully created")

	context = {'form':form}


	return render(request,'create.html',context)



def genre_detail(request,id=None):
	instance = get_object_or_404(Genre,id=id)
	context = {'instance':instance}
	return render(request,"details.html",context)
	# return HttpResponse('<h1>detail</h1>')

def genre_list(request):
	instance = Genre.objects.all()
	context = {'instance':instance}
	query = request.GET.get("q")
	if query:
		instance = instance.filter(genre__icontains=query)
		context = {'instance':instance}
	return render(request,'base.html',context)

def genre_update(request,id=None):
	instance = get_object_or_404(Genre,id=id)
	form = GenreForm(request.POST or None,instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	context = {'instance':instance,'form':form}

	return render(request,'create.html',context)


def genre_delete(request,id=None):
	instance = get_object_or_404(Genre,id=id)
	instance.delete()
	messages.success(request, 'Delete Successful')
	return HttpResponseRedirect('/music/')

def music_create(request):
	form = MusicForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"succesfully created")

	context = {'form':form}
	return render(request,'music_create.html',context)

def music_detail(request,id=None):
	instance = get_object_or_404(Music,id=id)
	context = {'instance':instance}
	return render(request,"music_details.html",context)
	# return HttpResponse('<h1>detail</h1>')

def music_list(request):
	instance = Music.objects.all()
	context = {'instance':instance}
	query = request.GET.get("q")
	if query:
		instance = instance.filter(music_title__icontains=query)
		context = {'instance':instance}
	return render(request,'music_base.html',context)

def music_update(request,id=None):
	instance = get_object_or_404(Music,id=id)
	form = MusicForm(request.POST or None,instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	context = {'instance':instance,'form':form}

	return render(request,'music_create.html',context)


def music_delete(request,id=None):
	instance = get_object_or_404(Music,id=id)
	instance.delete()
	messages.success(request, 'Delete Successful')
	return HttpResponseRedirect('/song/list')

