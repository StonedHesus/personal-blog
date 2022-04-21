from django.contrib import admin
from .models import Post

# Register your models here.

# Register the Post object on the administration site.
admin.site.register(Post)