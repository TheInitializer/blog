from django.contrib import admin

from .models import Post, Image

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'date')

admin.site.register(Post, PostAdmin)

class ImageAdmin(admin.ModelAdmin):
	list_display = ('admin_thumbnail', 'admin_filename')

admin.site.register(Image, ImageAdmin)
