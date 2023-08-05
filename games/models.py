from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()

    
class Genre(models.Model):
    name = models.CharField(_("Name"), max_length=150)
    parent = models.ForeignKey("self", related_name="children", on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
    
class Platform(models.Model):
    PS = 1
    XBOX = 2
    NIN = 3
    PC = 4
    SD = 5
    platforms = (
        (PS,"playStation"),
        (XBOX, "Xbox"),
        (NIN, "Nintendo"),
        (PC, "Pc"),
        (SD, "SteamDeck"),
    )
    name = models.PositiveSmallIntegerField(_("Name"), choices=platforms, default=PS)
    description = models.TextField(_("Description"), null=True, blank=True)
    
    def __str__(self):
        return self.get_name_display()
    
    
class Company(models.Model):
    name = models.CharField(_("Name"), max_length=150)
    slug = models.SlugField(_("Company slug"), unique=True, max_length=250)
    found_year = models.DateField(_("Year founded"), null=True)
    description = models.TextField(_("Description"), null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.found_year}"
    

class Game(models.Model):
    title = models.CharField(_("Title"), max_length=200, unique=False)
    slug = models.SlugField(_("Game Slug"), max_length=250, unique=True, validators=[])
    release_date = models.DateField(_("Release Date"))
    score = models.PositiveSmallIntegerField(_("Score"), validators=[])
    description = models.TextField(_("Description"), null=True, blank=True)
    metacritic_link = models.URLField(_("Metacritic"), validators=[])
    must_paly = models.BooleanField(_("Must Play") ,default=False)
    image = models.ImageField(_("Images"), upload_to="images/", null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="games", verbose_name=_("Genre"))
    platform = models.ForeignKey(Platform, on_delete=models.PROTECT, related_name="games", verbose_name=_("Platform"))
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="games", verbose_name=_("Company"), null=True)
    def __str__(self):
        return f"{self.title} - {self.release_date} "
    
    
    
    
class HowLongToBeat(models.Model):
    FULL = 1
    STORY_N = 2
    STORY_H = 3
    type = (
        (FULL, "FullComplete"),
        (STORY_N, "NormalStory"),
        (STORY_H, "HardStory"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hltb")
    time = models.TimeField(_("Time"))
    mode = models.PositiveSmallIntegerField(choices=type, default=STORY_N)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="hltb")
    
    
# class Rate(models.Model):
#     game = models.ForeignKey(Game, related_name="rates", on_delete=models.CASCADE, verbose_name=_("Game"))
#     user = models.ForeignKey(User, related_name="rates", on_delete=models.CASCADE, verbose_name=_("User"))
#     rate = models.PositiveIntegerField(_("Rate"), validators=[])
    
    
    
# class Comment(models.Model):
#     game = models.ForeignKey(Game, related_name="comments", on_delete=models.CASCADE, verbose_name=_("Game"))
#     user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE, verbose_name=_("User"))
#     content = models.TextField(_("Content"))
#     time = models.DateField(auto_now_add=True)