from django.contrib import admin

# Register your models here.
from personal.models import Bio, File, Post, LinkPost

admin.site.register(Bio)
admin.site.register(File)
admin.site.register(Post)
admin.site.register(LinkPost)
