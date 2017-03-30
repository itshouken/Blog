from django.contrib import admin
from .models import Post #now that we have Post as one of our models
# Register your models here.

admin.site.register(Post)
