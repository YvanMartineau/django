from django.contrib import admin
from .models import Post, Comment

#Register them in the admin interface
admin.site.register(Post)
admin.site.register(Comment)
