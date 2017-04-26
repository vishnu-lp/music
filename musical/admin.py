from django.contrib import admin
from .models import Genre,Music

# Register your models here.la

class GenreAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('genre',)}
	list_display = ['genre','slug']

admin.site.register(Genre,GenreAdmin)


class MusicAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('music_title',)}
	list_display = ['genre','slug','music_title','rating']

admin.site.register(Music,MusicAdmin)
