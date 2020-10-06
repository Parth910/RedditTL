from django.contrib import admin

# Register your models here.
from User.models import Auth, Post

admin.site.register(Auth)
admin.site.register(Post)