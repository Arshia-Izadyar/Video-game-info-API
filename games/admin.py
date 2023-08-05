from django.contrib import admin

from .models import Game, Genre, Platform, Company


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "description")
    
    
@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display= ("name", "description")

    

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'score', "genre", "platform")
    search_fields = ("title", "genre")
    list_filter = ("platform",)
    
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id","name", "found_year")
    search_fields = ("name",)
    
    
