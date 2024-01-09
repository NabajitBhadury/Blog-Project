from django.contrib import admin
from .models import Post
from .models import Image
# Register your models here.
admin.site.register(Image)
admin.site.register(Post)
