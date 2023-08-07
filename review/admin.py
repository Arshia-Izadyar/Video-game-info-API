from django.contrib import admin
from .models import Comment, Rate


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "time")
    
@admin.register(Rate)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "rate")
