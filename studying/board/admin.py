from django.contrib import admin
from .models import Board, Photo

# Register your models here.


class PhotoInline(admin.TabularInline):
    model = Photo
class BoardAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]

admin.site.register(Board, BoardAdmin)
