from django.contrib import admin
from form import form
from rest_framework import request


from .models import Post

admin.site.register(Post)


