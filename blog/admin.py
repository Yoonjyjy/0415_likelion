from django.contrib import admin
from .models import Post

## models 앞에 있는 .은 현재 폴더를 의미

# Register your models here.
admin.site.register(Post)