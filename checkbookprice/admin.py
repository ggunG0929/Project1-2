from django.contrib import admin
from .models import Photo

# 관리자페이지에서 photo 관리가능
admin.site.register(Photo)
